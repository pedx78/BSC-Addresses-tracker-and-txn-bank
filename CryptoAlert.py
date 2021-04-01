import webbrowser
import requests
import json
import confidential
import time

ApiKey = confidential.get_BSC_API_KEY()
whale1 = "0xcC64ea842FcDe4283CF239259f7462Ef809c44FD"
whales = ["0xcC64ea842FcDe4283CF239259f7462Ef809c44FD",
         "0x7238B14Ed465991EecCB9346cf435eE047dea6eD",
          "0x86B695aaa2600668CEC754C7827357626B188054",
          "0x2c46B8fdCBe827A814DA412FF1EBDc2544e683c1",
          "0xA803fc1c1e83d6389865e1248Dc924ed4C6953De",
          "0x0C8C62A7F883C6E47c8C5790474d4Eb8a48924f2",
          "0x82dE83D35f6F95A87FA04328724d2063f834268F",
          "0x52C717CE5a6b483A890bCDC3114ff140E679B43F",
          "0x0D5872177064bc858c9dD926a02cE356a317727E",
          "0x2D338C5549F437CD5f35A1d8C7A244c048f9C00a"
          ]

# open web with overview of the whale
whaleOverview = "https://bscscan.com/address/"+whale1
webbrowser.open(whaleOverview, new=2)


def getBalance(whale):
    #Call balance command, pass whale address and personal BSC APIkey, open browser with balance
    whaleBalance = "https://api.bscscan.com/api?module=account&action=balance&address="+whale+"&tag=latest&apikey="+ApiKey+".json"
    #webbrowser.open(whaleBalance, new=2)

def getTransactions(whale):
    #Call tokens transactions command, pass whale address, number of results , and key. open browser with results
    transactions = "https://api.bscscan.com/api?module=account&action=tokentx&address="+whale+"&page=1&offset=1&sort=desc&apikey="+ApiKey+".json"
    #webbrowser.open(transactions, new=2)

    response = requests.get(transactions)
    DecodedTransactions = json.loads(response.text)
    token = (DecodedTransactions['result'][0]['tokenName'])

    value = float(DecodedTransactions['result'][0]['value'])
    tokenDecimal = DecodedTransactions['result'][0]['tokenDecimal']
    aumount = int(value)/int(10)**(int(tokenDecimal))
    contractAddress = DecodedTransactions['result'][0]['contractAddress']

    print("Token name: "+ token + " #tokens: " + str(aumount))
    print("Contract address: " + contractAddress)
    


for whale in whales:
    getBalance(whale)
    getTransactions(whale)
    time.sleep(1)


