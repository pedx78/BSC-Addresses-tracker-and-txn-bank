import webbrowser
import requests
import json
import confidential

ApiKey = confidential.get_BSC_API_KEY()
whale1 = "0xcC64ea842FcDe4283CF239259f7462Ef809c44FD"

# open web with overview of the whale
whaleOverview = "https://bscscan.com/address/"+whale1
webbrowser.open(whaleOverview, new=2)


def getBalance(whale):
    #Call balance command, pass whale address and personal BSC APIkey, open browser with balance
    whaleBalance = "https://api.bscscan.com/api?module=account&action=balance&address="+whale+"&tag=latest&apikey="+ApiKey+".json"
    webbrowser.open(whaleBalance, new=2)

def getTransactions(whale, interval):
    #Call tokens transactions command, pass whale address, number of results , and key. open browser with results
    transactions = "https://api.bscscan.com/api?module=account&action=tokentx&address="+whale+"&page=1&offset="+ str(interval) +"&sort=desc&apikey="+ApiKey+".json"
    webbrowser.open(transactions, new=2)

    response = requests.get(transactions)
    DecodedTransactions = json.loads(response.text)
    print(DecodedTransactions)
    print(DecodedTransactions['result'][0]['tokenName'])



getBalance(whale1)
getTransactions(whale1, 1)


