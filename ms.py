import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="hids",
    passwd="qwert123",
    database="home_data"
)

mycursor = mydb.cursor()

mycursor.execute('SHOW TABLES')

for i in mycursor:
    print(i)

mydb.close()