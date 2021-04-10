def get_name():
    return "Juan"
    
import pandas as pd
import datetime



whale = '0xcc64ea842fcde4283cf239259f7462ef809c44fd'
hash = '0xb300d5d61ab134e1fdc4bc93c182d5c0a2b30a95aba99b1d222875ca12c474e2'
token ='SafeMoon'
aumount = 22500000000.0
contractAddress='0x8076c74c5e3f5852037f31ff0093eeb8c8add8d3'
Age = '0:1:40:32'
action ='SELL'
Total_Balance = 64796480.35
Value_Dollars = 29578.58

a = ['0xcc64ea842fcde4283cf239259f7462ef809c44fd',
 '0xb300d5d61ab134e1fdc4bc93c182d5c0a2b30a95aba99b1d222875ca12c474e2',
 'SafeMoon',
  22500000000.0,
   '0x8076c74c5e3f5852037f31ff0093eeb8c8add8d3',
    '0:1:40:32',
     'SELL',
      64796480.35,
       29578.58]

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

temporal_panda = pd.DataFrame(columns = ['Address','Hash', 'Token', 'Aumount','TokenContract','Age','Action','Total_Balance','DOLLARS'])
print(temporal_panda)
temporal_panda.loc[0] = [a[0], a[1], a[2], a[3], a[4], a[5], a[6], a[7], a[8]]
#df.loc[1] = [whale, hash, token, aumount, contractAddress, Age, action, Total_Balance, Value_Dollars]

print(temporal_panda)

print(time.now())