test = {'status': '1',
 'message': 'OK',
  'result': [{'blockNumber': '6111934', 'timeStamp': '1617048483', 'hash': '0x3969d98d5fc68aff0eebaca57ba02a4af755354df2530bcf9004836a77f77dd7',
   'nonce': '91',
    'blockHash': '0xb6c41b0f2f1910637c76a2984cf26dcce633c8e26b49f8f3ed4ae809cadb25c2',
     'from': '0xb25122ab1e0e44d73b7c35e378201787bc9594ed',
      'contractAddress': '0x69af49e82ea59a97f3879547f67b913c216c3714',
       'to': '0xcc64ea842fcde4283cf239259f7462ef809c44fd',
        'value': '9400000', 'tokenName': 'UNITi', 'tokenSymbol': 'UNIT', 'tokenDecimal': '9', 'transactionIndex': '13', 'gas': '154734', 'gasPrice': '10000000000', 'gasUsed': '103156', 'cumulativeGasUsed': '2243418', 'input': 'deprecated', 'confirmations': '80877'}]}

print(test['result'][0]['timeStamp'])

whales = [{"0xcC64ea842FcDe4283CF239259f7462Ef809c44FD",5},
         {"0x7238B14Ed465991EecCB9346cf435eE047dea6eD",8}]

a = ('UNITi', 0.0094, '0x69af49e82ea59a97f3879547f67b913c216c3714')

from numpy.core.numeric import False_
import pandas as pd
from datetime import datetime
from datetime import timedelta

from pandas.io.pytables import Table


input_ = ['0xcC64ea842FcDe4283CF239259f7462Ef809c44FD', 'UNITi', 0.0094, '0x69af49e82ea59a97f3879547f67b913c216c3714', '3:5:20:55']
WhalesDataset = {'Address': [],
        'Token': [],
        'Aumount': [],
        'TokenContract': [],
        'Age': [],
        }

df = pd.DataFrame(WhalesDataset, columns = ['Address', 'Token', 'Aumount','TokenContract','Age'])



def addTable(info):
        df2 = pd.DataFrame([info], columns = ['Address', 'Token', 'Aumount','TokenContract','Age'])
        Table = df.append(df2, ignore_index=True)
        return Table
#print("new")

a = 'B4Bdv6'
print(a.lower())

whales = ["0xcc64ea842fcde4283cf239259f7462ef809c44fd",
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

def changeCase(whales):
    for whale in whales:
        whale = whale.lower()
        print(whale)

#changeCase(whales)

'''
def percentage_Invested(action, balance, value):
        if (action == "BUY") and (isinstance(balance, float)) and (isinstance(value, float)):
                perc = (value / balance) * 100
                solution = str(perc) + " %" 
                return solution
        else:
                return "SELL/NO $ VALUE"

print(percentage_Invested("SELL", 1000.0, 100.0))
'''


def timePassed(since):
    now = datetime.now()
    time_passed = now - since


def timeConverter(timestamp):
        solution = datetime.fromtimestamp(timestamp)
        return solution

#print(timeConverter(1617639691))
import random
def random_User():
        users = ["Mozilla/5.0 (Windows NT 6.3; WOW64)", "AppleWebKit/537.36 (KHTML, like Gecko)", "Chrome/47.0.2526.69", "Safari/537.36"]
        magic_number = random.randint(0, 3)
        print(users[magic_number])
random_User()

print("HELOOL\ngfgfg")