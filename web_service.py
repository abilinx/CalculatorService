from json import loads
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
import calculator_library


def calculate(request):
    print(f'HTTP request body: {request.body}')
    json_object = loads(request.body.decode('utf8'))
    print(f'calculator input: ' + json_object['statement'])
    try:
        result = calculator_library.calculate(json_object['statement'])
        response_body = '{"result": "' + str(result) + '"}'
        print(f'HTTP response body: {response_body}, status code: 200')
        return Response(response_body, status=200)
    except calculator_library.InputSyntaxError:
        print(f'No HTTP response body, status code: 400 calculator input error')
        return Response(status='400 calculator input error')


if __name__ == '__main__':
    with Configurator() as config:
        config.add_route('calculate', '/')
        config.add_view(calculate, route_name='calculate')
        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 6543, app)
    server.serve_forever()