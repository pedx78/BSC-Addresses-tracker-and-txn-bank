import mysql.connector
print("RUNNING")
mydb = mysql.connector.connect(
    host = "10.0.0.143",
    user = "root",
    passwd = "M0lusc0s436$",
    auth_plugin='mysql_native_password',
    database="CRYPTO_DATABASE"
)

mycursor = mydb.cursor()

'''
mycursor.execute("SHOW DATABASES")
for db in mycursor:
    print(db)
'''


mycursor.execute("CREATE TABLE temporal (Address VARCHAR(255), )")