import time,json
from urllib.request import urlopen

class App:
    def show(self, environ, start_response):
        status = '200 OK'
        result = '1'

        # Обработка поиска здесь. Данные для выдачи пользователю необходимо внести в переменную result в виде строки.

        start_response(status, [
            ('Content-Type', 'text/plain'),
            ('Content-Length', str(len(result)))
        ])
        return [result.encode('utf-8')]

    def save(self, environ, start_response):
        status = '200 OK'
        length = int(environ['CONTENT_LENGTH'])
        body = environ['wsgi.input'].read(length).decode('utf-8')

        print(environ['wsgi.input'],type(environ['wsgi.input']),length)

        print(urlopen(environ['wsgi.input']).read(length).decode('utf-8'))

        """
        mass = [i.split('=') for i in body.split('&')]
        data_time = time.strftime("%Y-%m-%d %H.%M", time.localtime(int(mass[0][1]))).split(' ')

        print(data_time)
        print(mass[1][1].replace('.',' '))
        print(mass[2][1].replace('+',' '))

        f = open('log.txt','a')
        f.write('Отправитель: '+mass[1][1].replace('.',' ')+' Дата: '+data_time[0]+' Время: '+data_time[1]+'\n')
        f.close()

        """
        # Обработка сохранения здесь. В body находится тело запроса в виде строки.

        start_response(status, [('Content-Length', '0')])
        return [b'']
