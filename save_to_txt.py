import time

class save_to_f:
    def __init__(self,data):
        for i in data:
            date = time.strftime("%Y-%m-%d %H.%M", time.localtime(int(i['time']))).split(' ')
            sender = i['sender']
            message = i['message']

            f = open('log.txt', 'a')
            f.write('Отправитель: ' + sender + ' Дата: ' + date[0] + ' Время: ' + date[1] +' Текст сообщения: '+message+ '\n')
            f.close()