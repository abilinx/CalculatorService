from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
import json


def calculate(request):
    print(f'body: {request.body}')
    json_object = json.loads(request.body.decode('utf8'))
    print(f'statement: ' + json_object['statement'])
    result = eval(json_object['statement'])
    return Response('{"result": "' + str(result) + '"}')


if __name__ == '__main__':
    with Configurator() as config:
        config.add_route('calculate', '/')
        config.add_view(calculate, route_name='calculate')
        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 6543, app)
    server.serve_forever()