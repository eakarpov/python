from random import randint
from time import sleep
from wsgiref.simple_server import make_server


def events(max_delay, limit):
    while True:
        delay = randint(1, max_delay)
        if delay >= limit:
            sleep(limit)
            yield None
        else:
            sleep(delay)
            yield 'Event generated, awaiting %d s' % delay


event_generator = events(10, 9)


class WSGIApplication:

    def __init__(self, environment, start_response):
        print('Get request')
        self.environment = environment
        self.start_response = start_response
        self.headers = [
            ('Content-type', 'text/plain: charset=utf-8')
        ]

    def __iter__(self):
        print('Wait for response')
        if self.environment.get('PATH_INFO', '/') == '/':
            event = next(event_generator)
            print(str(event))
            if event is None:
                self.no_content_response()
            else:
                yield from self.ok_response(event)
        else:
            yield from self.not_found_response()
        print('Done')

    def not_found_response(self):
        print('Create response')
        print('Get headers')
        self.start_response('404 Not found', self.headers)
        print('Headers are sent')
        yield('404 error').encode('utf-8')

    def no_content_response(self):
        print('Create response')
        print('Get status only')
        self.start_response('204 No Content', [])
        print('Status is sent')

    def ok_response(self, message):
        print('Create response')
        print('Get headers')
        self.start_response('200 OK', self.headers)
        print('Headers are sent')
        yield ('%s\n' % message).encode('utf-8')
        print('Body is sent')

if __name__ == '__main__':
    server = make_server('127.0.0.1', 80, WSGIApplication)
    server.serve_forever()

