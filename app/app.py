import time,json

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

        body = json.loads(environ['wsgi.input'].read(length).decode('utf-8')) # add loads from json dumps

        for i in range(len(body)):
            if i==0:
                start_date = body[i]['time']
            elif i==(len(body)-1):
                end_date = body[i]['time']

        start_date = time.strftime("%Y,%m,%d,%H,%M,%S", time.localtime(start_date))

        print(start_date, end_date)

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
