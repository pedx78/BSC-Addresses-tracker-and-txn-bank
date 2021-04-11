import random
def get_BSC_API_KEY():
    users = ["92MM9Q3NG1AHGE21YEHMX6F56VWM6GM3PW", "EVC2IFRX4NJ2IAMTK592SI8YX9YWPQCZWJ", "A5NDCHK6QBHRCXVSD2JHG9VMDQKPVZYHCE"]
    magic_number = random.randint(0, 2)
    return (users[magic_number])

#API KEYS
#92MM9Q3NG1AHGE21YEHMX6F56VWM6GM3PW
#EVC2IFRX4NJ2IAMTK592SI8YX9YWPQCZWJ
#A5NDCHK6QBHRCXVSD2JHG9VMDQKPVZYHCE

def J_Credentials():
    credentials = "10.0.0.143"
    return credentials

def S_Credentials():
    credentials = "localhost"
    return credentials

#print(J_Credentials())
#print(S_Credentials())






'''
def random_User():
    users = ["92MM9Q3NG1AHGE21YEHMX6F56VWM6GM3PW", "EVC2IFRX4NJ2IAMTK592SI8YX9YWPQCZWJ", "A5NDCHK6QBHRCXVSD2JHG9VMDQKPVZYHCE"]
    magic_number = random.randint(0, 3)
    return (users[magic_number])
'''
#print(get_BSC_API_KEY())

