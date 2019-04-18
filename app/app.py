import time,json
from ms import my_connect
from work_with_body import wwb
from save_to_txt import save_to_f

class App:
    def show(self, environ, start_response):
        status = '200 OK'
        result = ''

        db_connect = my_connect('localhost','hids','qwert123',"home_data")
        result = db_connect.test('dialogs')
        db_connect.close()
        # Обработка поиска здесь. Данные для выдачи пользователю необходимо внести в переменную result в виде строки.

        start_response(status, [
            ('Content-Type', 'text/plain'),
            ('Content-Length', str(len(result)))
        ])
        return [result.encode('cp1251')]

    def save(self, environ, start_response):
        status = '200 OK'
        length = int(environ['CONTENT_LENGTH'])

        body = json.loads(environ['wsgi.input'].read(length).decode('utf-8')) # add loads from json dumps

        our_data = wwb(body)

        db_connect = my_connect('localhost','hids','qwert123',"home_data")
        db_connect.ins('dialogs', our_data.start_date, our_data.end_date,our_data.lenth)
        db_connect.test('dialogs')
        db_connect.close()

        save_to_f(body)

        # Обработка сохранения здесь. В body находится тело запроса в виде строки.

        start_response(status, [('Content-Length', '0')])
        return [b'']
