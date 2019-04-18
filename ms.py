import mysql.connector, time
from datetime import datetime

class my_connect:
    def __init__(self, host, user, user_pas, db_name, start_time, end_time, lenth):

        self.mydb = mysql.connector.connect(
            host=host,
            user=user,
            passwd=user_pas,
            database=db_name
        )

        self.start_time = time.strftime("%Y,%m,%d,%H,%M,%S", time.localtime(start_time))
        self.end_time = time.strftime("%Y,%m,%d,%H,%M,%S", time.localtime(end_time))
        self.lenth = lenth
        self.mycursor = self.mydb.cursor()

    def ins(self, table_name):

        start_time = self.start_time.split(',')
        end_time = self.end_time.split(',')

        add_dialogs = ("INSERT INTO "+table_name+" "
                       "(start_time, end_time, message_count) "
                       "VALUES (%s, %s, %s)")

        data_input = (datetime(int(start_time[0]),int(start_time[1]),int(start_time[2]),int(start_time[3]),int(start_time[4]),int(start_time[5])),
                      datetime(int(end_time[0]),int(end_time[1]),int(end_time[2]),int(end_time[3]),int(end_time[4]),int(end_time[5])),
                      self.lenth)

        self.mycursor.execute(add_dialogs, data_input)

    def test(self, table_name):

        self.mycursor.execute('SELECT * FROM dialogs')
        for i in self.mycursor:
            print(i)

    def close(self):

        self.mydb.commit()
        self.mydb.close()

"""
table_name = 'dialogs'

a = my_connect('localhost','hids','qwert123',"home_data")

a.ins(table_name)
a.test(table_name)
a.close()
"""