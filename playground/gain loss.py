number_of_shares = int(input("Enter number of shares:"))
purchase_price = float(input("Enter purchase price:"))
sale_price = float(input("Enter sale price:"))

buy = float(number_of_shares * purchase_price)
first_commission = float(buy * .11)

sale = float(number_of_shares * sale_price)
second_commission = float(sale * .11)

net = float(sale - buy - first_commission - second_commission)
if net > 0:
    print("After the transaction, you gained", net, "dollars.")
if net < 0:
    print("After the transaction, you lost", net * -1, "dollars.")


import pandas as pd
#from tabulate import tabulate
import pytz
import datetime as dt
from datetime import date

# pass the API and prevDays (0 for today, 1 since yesterday...)
def report2(api, prevDays):
    #
    # get all closed orders and import them into a dataframe
    #
    orderTotal = 500
    today = dt.date.today() - dt.timedelta(days=prevDays)
    today = dt.datetime.combine(today, dt.datetime.min.time())
    today = today.strftime("%Y-%m-%dT%H:%M:%SZ")
    #print(today)
    orders = api.list_orders(status='all', limit=orderTotal, after=today)
    if not orders:
        return
    dfOrders = pd.DataFrame()
    for o in orders:
        # convert dot notation to dict
        d = vars(o)
        # import dict into dataframe
        df = pd.DataFrame.from_dict(d, orient='index')
        # append to dataframe
        dfOrders = dfOrders.append(df, ignore_index=True)

    # select filled orders with buy or sell
    dfSel = dfOrders
    # choose a subset (use .copy() as we are slicing and to avoid warning)
    dfSel = dfSel[['submitted_at', 'filled_at', 'symbol', 'filled_qty', 'side', 'type', 'filled_avg_price', 'status']].copy()

    # convert filled_at to date
    dfSel['submitted_at'] = pd.to_datetime(dfSel['submitted_at'], format="%Y-%m-%d %H:%M:%S")
    dfSel['filled_at']    = pd.to_datetime(dfSel['filled_at'], format="%Y-%m-%d %H:%M:%S")
    # convert to our timezone
    dfSel['submitted_at'] = dfSel['submitted_at'].dt.tz_convert('America/New_York')
    dfSel['filled_at']    = dfSel['filled_at'].dt.tz_convert('America/New_York')
    # remove millis
    dfSel['submitted_at'] = dfSel['submitted_at'].dt.strftime("%Y-%m-%d %H:%M:%S")
    dfSel['filled_at']    = dfSel['filled_at'].dt.strftime("%Y-%m-%d %H:%M:%S")

    # Sort: https://kanoki.org/2020/01/28/sort-pandas-dataframe-and-series/
    # need to sort in order to perform the proper calculations
    # sort based on the following sequence of types: market then limit, then stop_limit
    dfSel['type'] = pd.Categorical(dfSel['type'], categories=["market", "limit", "stop_limit"])
    # sort first based on symbol, then type as per the list above, then submitted date
    dfSel.sort_values(by=['symbol', 'submitted_at', 'type'], inplace=True, ascending=True)

    # reset index
    dfSel.reset_index(drop=True, inplace=True)
    # drop the 'side' column
    # dfProfit = dfSel.drop('side', 1)
    dfProfit = dfSel
    # add empty 'profit' column
    dfProfit['profit'] = ''

    totalProfit = 0.0
    profitCnt   = 0
    lossCnt     = 0
    slCnt       = 0
    ptCnt       = 0
    trCnt       = 0
    qty         = 0
    profit      = 0
    sign        = {'buy': -1, 'sell': 1}

    # show header row
    #print(tabulate(dfSel[:0], headers='keys', tablefmt='simple', showindex=False))

    for index, row in dfSel.iterrows():
        # show data row
        #print(index, tabulate(dfSel[index:index+1], headers='', tablefmt='plain'))

        # conditions:
        # - buy/sell have the same symbol
        # - a trade is considered if no new/held orders are still open
        # - once qty is 0 a complete trade is confirmed and profit calculated
        # - a filled_avg_price is not None

        if index > 0:
            if dfSel['symbol'][index - 1] != dfSel['symbol'][index]:
                qty    = 0
                profit = 0

        if dfSel['status'][index] == 'held':
            continue
        if dfSel['status'][index] == 'new':
            continue
        if dfSel['filled_avg_price'][index] is None:
            continue
        if dfSel['filled_avg_price'][index] == '':
            continue
        if dfSel['filled_avg_price'][index] == 'None':
            continue

        #print(index, tabulate(dfSel[index:index+1], headers='', tablefmt='plain'))

        side      = dfSel['side'][index]
        filledQty = int(dfSel['filled_qty'][index]) * sign[side]
        qty       = qty + filledQty
        price     = float(dfSel['filled_avg_price'][index])
        pl        = filledQty * price
        profit    = profit + pl

        #print(f"{dfSel['symbol'][index]}: qty {filledQty} price {price} profit {profit:.3f}")

        if qty==0:
            # complete trade
            trCnt = trCnt + 1
            # put the profit in its column
            #dfProfit['profit'][index] = profit
            dfProfit.loc[index, 'profit'] = round(profit, 2)
            totalProfit = totalProfit + profit
            if profit >= 0:
                profitCnt = profitCnt + 1
                if dfSel['type'][index] == 'limit':
                    ptCnt = ptCnt + 1
            else:
                lossCnt = lossCnt + 1
                if dfSel['type'][index] == 'stop_limit':
                    slCnt = slCnt + 1
            profit = 0

    # append the total
    dfProfit.loc["Total", "profit"] = round(totalProfit, 2)  # dfProfit.profit.sum()

    # print profit report
    print(tabulate(dfProfit, headers='keys', tablefmt='simple', showindex=True, floatfmt=".2f"))
    #print(dfProfit.to_string())

    totalCnt = profitCnt + lossCnt
    if totalCnt > 0:
        ratio = profitCnt / totalCnt * 100.0
        print('\nProfits:', profitCnt)
        print('Losses :'  , lossCnt)
        print('Ratio  :'  , f'{ratio:.2f}%')
        print('Trades :'  , trCnt)
        print('Stops  :'  , slCnt)
        print('Targets:'  , ptCnt)