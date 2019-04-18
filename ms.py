import mysql.connector
from datetime import datetime

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

add_dialogs = ("INSERT INTO dialogs "
               "(start_time, end_time, message_count) "
               "VALUES (%s, %s, %s)")

data_input = (datetime(2019,2,26,15,17,25), datetime(2019,2,26,18,17,25), '3')

mycursor.execute(add_dialogs, data_input)

mycursor.execute('SELECT * FROM dialogs')
for i in mycursor:
    print(i)

mydb.commit()

mydb.close()