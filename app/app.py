class App:
    def show(self, environ, start_response):
        status = '200 OK'
        result = ''

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

        # Обработка сохранения здесь. В body находится тело запроса в виде строки.

        start_response(status, [('Content-Length', '0')])
        return [b'']
