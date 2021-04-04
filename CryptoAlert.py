import webbrowser
from numpy.lib.arraypad import _set_wrap_both
from pandas.core.dtypes.missing import notnull
from pandas.io.pytables import Table
import requests
import json
import confidential
import time

import numpy as np
import pandas as pd
from datetime import datetime
from datetime import timedelta

import w



ApiKey = confidential.get_BSC_API_KEY()
whale1 = "0xcC64ea842FcDe4283CF239259f7462Ef809c44FD"
whales = ["0xcc64ea842fcde4283cf239259f7462ef809c44fd",
         "0x7238b14ed465991eeccb9346cf435ee047dea6ed",
          "0x86b695aaa2600668cec754c7827357626b188054",
          "0x2c46b8fdcbe827a814da412ff1ebdc2544e683c1",
          "0xa803fc1c1e83d6389865e1248dc924ed4c6953de",
          "0x0c8c62a7f883c6e47c8c5790474d4eb8a48924f2",
          "0x82de83d35f6f95a87fa04328724d2063f834268f",
          "0x52c717ce5a6b483a890bcdc3114ff140e679b43f",
          "0x0d5872177064bc858c9dd926a02ce356a317727e",
          "0x2d338c5549f437cd5f35a1d8c7a244c048f9c00a"
          ]

def changeCase(whales):
    for whale in whales:
        whale = whale.lower()
        print(whale)


# open web with overview of the whale
whaleOverview = "https://bscscan.com/address/"+whale1
webbrowser.open(whaleOverview, new=2)



def timeConverter(timestamp):
        solution = datetime.fromtimestamp(timestamp)
        return solution

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

def getBalance(whale):
    #Call balance command, pass whale address and personal BSC APIkey, open browser with balance
    whaleBalance = "https://api.bscscan.com/api?module=account&action=balance&address="+whale+"&tag=latest&apikey="+ApiKey+".json"
    #webbrowser.open(whaleBalance, new=2)

def txn_direction(whale, from_):
    
    whale = whale.lower()
    if (whale != from_):
        return "BUY"
    elif(whale == from_):
        return "SELL"
    else:
        return "ERROR"
        
    


def getTransactions(whale):

    #Whale BSC website for webScarpping
    Total_Balance = w.getTokenBalance(whale)
    #Call tokens transactions command, pass whale address, number of results , and key. open browser with results
    transactions = "https://api.bscscan.com/api?module=account&action=tokentx&address="+whale+"&page=1&offset=1&sort=desc&apikey="+ApiKey+".json"
    
    #Fetch response json
    response = requests.get(transactions)
    DecodedTransactions = json.loads(response.text)

    #Individual attributes

    #Direction
    from_ = DecodedTransactions['result'][0]['from']
    contractAddress = DecodedTransactions['result'][0]['contractAddress']
    to_ = DecodedTransactions['result'][0]['to']
    action = txn_direction(whale,from_)
    #Values
    token = (DecodedTransactions['result'][0]['tokenName'])
    value = float(DecodedTransactions['result'][0]['value'])
    tokenDecimal = DecodedTransactions['result'][0]['tokenDecimal']
    aumount = int(value)/int(10)**(int(tokenDecimal))
    #Time
    timeStamp = timeConverter(int(DecodedTransactions['result'][0]['timeStamp']))
    Age = timePassed(timeStamp)
    #print("Token name: "+ token + " #tokens: " + str(aumount))
    #print("Contract address: " + contractAddress)
    hash = (DecodedTransactions['result'][0]['hash'])

        #Get txn value on dollars
    Value_Dollars = w.getTxnValue(hash, action)

    

    #print(whale)
    #print(from_)

   
    return [whale, hash, token, aumount, contractAddress, Age, action, Total_Balance, Value_Dollars]

WhalesDataset = {'Address': [],
        'Hash': [],
        'Token': [],
        'Aumount': [],
        'TokenContract': [],
        'Age': [],
        'Action': [],
        'Total_Balance': [],
        'Value $': []
        }
df = pd.DataFrame(WhalesDataset, columns = ['Address','Hash', 'Token', 'Aumount','TokenContract','Age','Action','Total_Balance','Value $'])

def addTable(info):
        df2 = pd.DataFrame([info], columns = ['Address','Hash', 'Token', 'Aumount','TokenContract','Age','Action','Total_Balance','Value $'])
        Table = df.append(df2, ignore_index=True)
        return Table




for whale in whales:
    getBalance(whale)
    print(addTable(getTransactions(whale)))
    time.sleep(0.1)


    



