import mysql.connector
#print("RUNNING")
mydb = mysql.connector.connect(
    host = "10.0.0.143",
    user = "root",
    passwd = "M0lusc0s436$",
    auth_plugin='mysql_native_password',
    database="CRYPTO_DATABASE"
)


'''
mycursor.execute("SHOW DATABASES")
for db in mycursor:
    print(db)
'''
#mycursor.execute("CREATE TABLE test (Address VARCHAR(50), Total_Balance FLOAT(14), Hash VARCHAR(70), Action VARCHAR(6), Aumount FLOAT(50), Token VARCHAR(50), TokenContract VARCHAR(50), DOLLARS FLOAT(8), Invested FLOAT(40), Age DATETIME NOT NULL)")
#mycursor.execute("SHOW TABLES")
#for db in mycursor:
#    print(db)

from datetime import datetime

sqlFormula = "INSERT INTO test (Address, Total_Balance, Hash, Action, Aumount, Token, TokenContract, DOLLARS, Invested, Age) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
#firstEntry = ('0xcc64ea842fcde4283cf239259f7462ef809c44fd', 70268805.2, '0xaf8863d22d2d6116b606fdf897e9452038d3076a95e4ff78ad7352f0be1bd20c', 'SELL', 45000000000.0, 'SafeMoon', '0x8076c74c5e3f5852037f31ff0093eeb8c8add8d3', 51900.8, 0.0, datetime(2021, 4, 5, 12, 37, 27))

#mycursor.execute(sqlFormula, firstEntry)
#mydb.commit()
'''
manyEntries = [('0xcc64ea842fcde4283cf239259f7462ef809c44fd', 53165994.98, '0xaf8863d22d2d6116b606fdf897e9452038d3076a95e4ff78ad7352f0be1bd20c', 'SELL', 45000000000.0, 'SafeMoon', '0x8076c74c5e3f5852037f31ff0093eeb8c8add8d3', 51963.51, 0.0, datetime.datetime(2021, 4, 5, 12, 37, 27)), ('0x7238b14ed465991eeccb9346cf435ee047dea6ed', 1342.62, '0x99266dd3b03f3693f84c1fb56b2bd25c4ccdce94fc34f464138122b7182a7a4b', 'SELL', 4834.887054423833, 'Binance-Peg BUSD Token', '0xe9e7cea3dedca5984780bafc599bd69add087d56', 4836.94, 0.0, datetime.datetime(2021, 4, 5, 13, 24, 55)), ('0x86b695aaa2600668cec754c7827357626b188054', 25286670.55, '0x07c2ab9c2e45aa34bc37124fad7f4d2812ab646242765383fdf1e9fcfd503e96', 
'SELL', 45000000000.0, 'SafeMoon', '0x8076c74c5e3f5852037f31ff0093eeb8c8add8d3', 59109.7, 0.0, datetime.datetime(2021, 4, 4, 22, 27, 10)), ('0x2c46b8fdcbe827a814da412ff1ebdc2544e683c1', 1617158.29, '0xace6c918c6484b35ec4086ff2b466ca6f54086ed207e383271bafd6ed3f52fdd', 'SELL', 339300000.0, 'SafeMoon', '0x8076c74c5e3f5852037f31ff0093eeb8c8add8d3', 376.86, 0.0, datetime.datetime(2021, 4, 5, 14, 18, 15)), ('0xa803fc1c1e83d6389865e1248dc924ed4c6953de', 4916172.6, '0xf9d102645dab75b8609e9c304100e7d86e04cb07332a2dd69325b03caa8b7068', 'BUY', 72.20253149198838, 'SyrupBar Token', '0x009cf7bc57584b7998236eff51b98a168dcea9b0', 0.01, 0.0001, datetime.datetime(2021, 4, 4, 15, 44, 12)), ('0x0c8c62a7f883c6e47c8c5790474d4eb8a48924f2', 11758953.9, '0x71196a7c323a239ae5dca8fe2dfe9dda27c648bf05939d98cc1c0a5398fbfb83', 'BUY', 4883932712533.221, 'FairEclipse', '0x4f45f6025be6c65573daa0b9965a75e837848da0', 11492.77, 0.09773633009990795, datetime.datetime(2021, 4, 5, 14, 19, 48)), ('0x82de83d35f6f95a87fa04328724d2063f834268f', 5.0, '0xffe5b2251bda585c249e7f45f698bdfc756c98fd2f9d78059883047030a5f444', 'SELL', 12132304024060.777, 'SafeStar', '0x3c00f8fcc8791fa78daa4a480095ec7d475781e2', 286322.37, 0.0, datetime.datetime(2021, 3, 21, 1, 31, 1)), ('0x52c717ce5a6b483a890bcdc3114ff140e679b43f', 1544602.87, '0x585f93a99582d424751264425d875847e2e5091b29f6911461cb184d65879c3a', 'BUY', 120000.0, 'SCARCITY', '0xb47083e6ffb691988cd1ec3efe5868c75fc34b66', 'SMALL RPS', 0.0, datetime.datetime(2021, 4, 5, 14, 39, 9)), ('0x0d5872177064bc858c9dd926a02ce356a317727e', 469612.78, '0xb0b87ab0cdf4761f60d7775a6f285de0ce9755a3f471502cb8bf6500c0ac94e5', 'BUY', 1800.0, 'PYXIS (pyxis.network)', '0x3ebb316d8c387ef235baa38978cbb9b97c8c3017', None, 0.0, datetime.datetime(2021, 3, 31, 11, 22, 52)), ('0x2d338c5549f437cd5f35a1d8c7a244c048f9c00a', 466620.65, '0xa07fb6746da91f77d6d39229cb0cb8e6240c59c3737351133ab186a85f575728', 'SELL', 23006482.687822856, 'SnowgeCoin', '0x5e9280d53f28281ce098c8f64e49f5f5dc9ea185', 11840.78, 0.0, datetime.datetime(2021, 4, 5, 15, 55, 27))]

mycursor.executemany(sqlFormula, manyEntries)
mydb.commit()
'''

mycursor = mydb.cursor()
#input = '0x68eafb3ef3ad17283ed9a0289ee4adcb054d946c6c951747e3734c5ade58c6e6'


def insert_sting_middle(str, word):
	return str[:2] + word + str[:2]

def check_hash_diplucate(hash):
    call = "SELECT count(Hash) from test where Hash = " + insert_sting_middle("'", hash)
    mycursor.execute(call)
    for c in mycursor:
        result = sum(c)
        return result

def Hash_in_module(hash):
    return hash
    
print(check_hash_diplucate('0xa07fb6746da91f77d6d39229cb0cb8e6240c59c3737351133ab186a85f575728'))



