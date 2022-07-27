from http.server import BaseHTTPRequestHandler
from http import HTTPStatus

URL_BASE = 'localhost'
PORT = 8000
LOCALHOST_URL = f'{URL_BASE}:{PORT}'


class Handler(BaseHTTPRequestHandler):

    def _parse_path(self):
        service, params_string = self.path.split('?')
        params = {
            param.split('=')[0]: param.split('=')[1]
            for param in params_string.split('&')
        }
        print(params)

    def _debugging_method(self):
        # TODO: Delete after delivery to main.
        print(self.path)

    def do_GET(self):
        self._debugging_method()
        self._parse_path()
        self.send_response(HTTPStatus.OK)
        self.send_header('Content-type','text/html')
        self.end_headers()

        message = "Too hot"
        self.wfile.write(bytes(message, "utf8"))

    def do_POST(self):
        self._debugging_method()
        self._parse_path()
        self.send_response(HTTPStatus.OK)
        self.send_header('Content-type','text/html')
        self.end_headers()

        message = "Hello, World! Here is a POST response"
        self.wfile.write(bytes(message, "utf8"))
