import webbrowser
#from numpy.lib.arraypad import _set_wrap_both
#from pandas.core.dtypes.missing import notnull
#from pandas.io.pytables import Table
import requests
from urllib.request import Request, urlopen
import json
import confidential
import time

import pandas as pd
from datetime import datetime
from datetime import timedelta

import WebScrapper as w
import mySql_Interaction as SQL
import whatsappMessage as WM


#while True:



print("Running...")

ApiKey = confidential.get_BSC_API_KEY()
whales = ["0xfd640bdb374729fe78d24bbe4e5b8faf83ae2ed5",
        "0x3fb7b0eed0efda15760f81f356f90d20de40b59f",
        "0x0c8c62a7f883c6e47c8c5790474d4eb8a48924f2",
        "0x01fb09f658fd186c4033500ae798917cacfda132",
        "0xc6c8978c4a213ebde8734432c75a7b5409999999",
        "0xbf8d5eb2723c3ab4bbd7527efb38c8e83d43832b",
        "0x511411d1a19be5259694b06f403c83f21a10258b",
        "0x326ea036c2bf0021f3909ab08cf8c230c7bfc4d5",
        "0x2da133db4c0084c4ffe55cb656c81ccc0543216f",
        "0x7238b14ed465991eeccb9346cf435ee047dea6ed",
        "0x4cf5a42f10b11758ddb579dfb637d533ea858b43",
        "0xc02bafe7adc61ea8ec89c5e8eb391bb947ed222e",
        "0x4b44c71c34ecd2f64c1a4223149a2b39ca113f98",
        "0x2c46b8fdcbe827a814da412ff1ebdc2544e683c1",
        "0x82de83d35f6f95a87fa04328724d2063f834268f",
        "0x52c717ce5a6b483a890bcdc3114ff140e679b43f",
        "0x0d5872177064bc858c9dd926a02ce356a317727e",
        "0x2d338c5549f437cd5f35a1d8c7a244c048f9c00a",
        "0xcc64ea842fcde4283cf239259f7462ef809c44fd",
        "0x86b695aaa2600668cec754c7827357626b188054",
        "0x8c7de13ecf6e92e249696defed7aa81e9c93931a",
        "0xa803fc1c1e83d6389865e1248dc924ed4c6953de",
        "0xd3dcccbb8466cd22f090452cd0ffdb05f2e73dd3",
        "0x1bbea62a08927c4b16493b5c20ab69b9dba295e0"
        ]

#   [UTILITY]   change Address to all lowerCase
def changeCase(whales):
    for whale in whales:
        whale = whale.lower()
        print(whale)


#   [OPTION]   open web with overview of address on variable
whale1 = "0xcC64ea842FcDe4283CF239259f7462Ef809c44FD"
def view_BSC_page(address):
    whaleOverview = "https://bscscan.com/address/"+ address
    webbrowser.open(whaleOverview, new=2)


#   [MAIN]  Transform Unix Epoch time to datetime
def timeConverter(timestamp):
        solution = datetime.fromtimestamp(timestamp)
        return solution

#   [OPTION]    Display time passed since Unit Epoch Time
def timePassed(since):
    now = datetime.now()
    time_passed = now - since
    time = time_passed.total_seconds()
    day = time // (24 * 3600)
    time = time % (24 * 3600)
    hour = time // 3600
    time %= 3600
    minutes = time // 60
    time %= 60
    seconds = time
    solution =  "%d:%d:%d:%d" % (day, hour, minutes, seconds)
    return solution

#   [OPTION]    Get Balance on BNB of Address (on development)
#def getBalance(whale):
    #Call balance command, pass whale address and personal BSC APIkey, open browser with balance
    #whaleBalance = "https://api.bscscan.com/api?module=account&action=balance&address="+whale+"&tag=latest&apikey="+ApiKey+".json"
    #webbrowser.open(whaleBalance, new=2)

#   [MAIN]  Return Transaction Direction -BUY SELL ERROR-
def txn_direction(whale, from_):
    whale = whale.lower()
    if (whale == from_):
        return "SELL"
    elif(whale != from_):
        return "BUY"
    else:
        return "ERROR"

#   [MAIN]  Return % Invested
def percentage_Invested(action, balance, value):
        if (action == "BUY") and (isinstance(balance, float)) and (isinstance(value, float)):
                perc = (value / balance) * 100
                perc = max(0.0001, perc)
                # Uncomment next for reciving a str
                #solution = str(perc) + " %" 
                return float(perc)
        else:
                return float(0.0)

import random
import urllib

    
#   [MAIN ROOT]   Fetch all info 
#@retry((Exception), tries=3, delay=0, backoff=0)

def getTransactions(whale):
    #try:

    # WebScarpping for the balance in tokens
    Total_Balance = w.getTokenBalance(whale)

    # BSC API MAIN RESPONSE 
    transactions = "https://api.bscscan.com/api?module=account&action=tokentx&address="+whale+"&page=1&offset=1&sort=desc&apikey="+ApiKey+".json"
    #print(transactions)
    # Fetch response json 
    '''
    #OUTDATED DUE ERROR 403 FORBIDDEN
    response = requests.get(transactions)
    #print(response.text)
    DecodedTransactions = json.loads(response.text)

    #DecodedTransactions = requests.get(transactions).json
    #print(DecodedTransactions)
   
    '''
    
    headers = {'User-Agent': 'XYZ/3.0'}
    #webbrowser.open(transactions, new=2)

    req = Request(transactions , headers=headers)    
    response = urlopen(req).read()
    DecodedTransactions = json.loads(response) 
    #print(response)
    
    



    # Individual attributes

    #Direction
    from_ = DecodedTransactions['result'][0]['from']
    #to_ = DecodedTransactions['result'][0]['to']
    action = txn_direction(whale,from_)

    #Token related
    token = (DecodedTransactions['result'][0]['tokenName'])
    contractAddress = DecodedTransactions['result'][0]['contractAddress']
    value = float(DecodedTransactions['result'][0]['value'])
    tokenDecimal = DecodedTransactions['result'][0]['tokenDecimal']
    aumount = int(value)/int(10)**(int(tokenDecimal))

    # Get Time
    timeStamp = timeConverter(int(DecodedTransactions['result'][0]['timeStamp']))
    Age = timeStamp

    #[OPTION] Show time passed since timestamp
    #Age = timePassed(timeStamp)
    
    #Hash
    hash = (DecodedTransactions['result'][0]['hash'])

    #Get txn value on dollars
    Value_Dollars = w.getTxnValue(hash, txn_direction(whale,from_))

    #Get percentage invested
    invested  = percentage_Invested(action, Total_Balance, Value_Dollars)

    #print(Age)
    #print(type(Age))

    
    #[OPTION] print results as they are fetched
    #print((whale, Total_Balance, hash, action, aumount, token, contractAddress, Value_Dollars, invested, Age))

    return (whale, Total_Balance, hash, action, aumount, token, contractAddress, Value_Dollars, invested, Age)
#except urllib.error.HTTPError:
#    print("FORBIDDEN ---------------- 0")
#    if error_counter < 3:
#        print(error_counter)
#        print(error_counter + 1)






WhalesDataset = {'Address': [],
        'Hash': [],
        'Token': [],
        'Aumount': [],
        'TokenContract': [],
        'Age': [],
        'Action': [],
        'Total_Balance': [],
        'DOLLARS': []
        }
#df = pd.DataFrame(columns = ['Address','Total_Balance', 'Hash', 'Action', 'Aumount', 'Token', 'TokenContract', 'DOLLARS', '% Invested', 'Age'])



temporal_panda = pd.DataFrame(columns = ['Address','Total_Balance', 'Hash', 'Action', 'Aumount', 'Token', 'TokenContract', 'DOLLARS', '% Invested', 'Age'])
def add_to_temporal(a, index):

    temporal_panda.loc[index] = [a[0], a[1], a[2], a[3], a[4], a[5], a[6], a[7], a[8], a[9]]
    



import mysql.connector

mydb = mysql.connector.connect(
    host = confidential.S_Credentials(),
    user = "root",
    passwd = "M0lusc0s436$",
    auth_plugin='mysql_native_password',
    database="CRYPTO_DATABASE"
)

mycursor = mydb.cursor()

sqlFormula = "INSERT INTO test (Address, Total_Balance, Hash, Action, Aumount, Token, TokenContract, DOLLARS, Invested, Age) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"



whale_index = 0

for whale in whales:
    
    #getBalance(whale)
    print("Fetching Information for Whale: " + whale)
    
    def Results():
        result = getTransactions(whale)
        hash_ = result[2]
        #print("HASH IN SCRIPT")
        #print(hash_)
        #print(result)
        #print("--------------")
        #print("RESULT:")
        print("Number of same entries on database: " + str(SQL.check_hash_diplucate(hash_)))
        if SQL.check_hash_diplucate(hash_) == 0:
            print("commiting....")
            mycursor.execute(sqlFormula, result)
            mydb.commit()
            print("COMMITED")
            if (result[1] > 1000000) or (whale == "0x3fb7b0eed0efda15760f81f356f90d20de40b59f"):
                WM.SendEmail(result)
                print("Alert Email Sent as Balance is > $1,000,000\n")
            else:
                print("No Email Sent as Balance is < $1,000,000\n")
        else:
            print("ENTRY ALREADY IN DATABASE\n")
    def two_tries():
        try:
            Results()
        except urllib.error.HTTPError:
            print("COULD NOT RETRIEVE INFO ON " + whale)
            print("Trying one more time: ")
            two_tries()
            #will break if it finds 2 errors
    
    two_tries()
    whale_index += 1
    if whale_index == len(whales):

        print("EXECUTED")

        
    
    '''
    add_to_temporal(getTransactions(whale), whale_index)
    whale_index += 1
    if whale_index == len(whales):
        print("---------- TEMPORAL TABLE WITH RESULTS ----------")
        pd.set_option('max_columns', None)
        print(temporal_panda)
    '''
    time.sleep(random.uniform(0.1, 1.5))



