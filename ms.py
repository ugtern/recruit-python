import mysql.connector
from datetime import datetime

class my_connect:
    def con(self, host, user, user_pas, db_name):

        mydb = mysql.connector.connect(
            host=host,
            user=user,
            passwd=user_pas,
            database=db_name
        )

        mycursor = mydb.cursor()
        return mycursor

    def ins(self, table_name, start_time, end_time):

        add_dialogs = ("INSERT INTO "+table_name+" "
                       "(start_time, end_time, message_count) "
                       "VALUES (%s, %s, %s)")

        data_input = (datetime(int(start_time[0]),int(start_time[1]),int(start_time[2]),int(start_time[3]),int(start_time[4]),int(start_time[5])),
                      datetime(int(end_time[0]),int(end_time[1]),int(end_time[2]),int(end_time[3]),int(end_time[4]),int(end_time[5])),
                      '3')

        self.mycursor.execute(add_dialogs, data_input)

    def test(self, table_name):

        self.mycursor.execute('SELECT * FROM dialogs')
        for i in self.mycursor:
            print(i)

    def close(self):

        self.mydb.commit()
        self.mydb.close()

start_time = '2019,2,26,15,17,25'.split(',')
end_time = '2019,2,26,18,17,25'.split(',')
table_name = 'dialogs'

a = my_connect.con('','localhost','hids','qwert123',"home_data")
my_connect.ins(a,table_name,start_time,end_time)