from http.server import BaseHTTPRequestHandler
from http import HTTPStatus

URL_BASE = 'localhost'
PORT = 8000
LOCALHOST_URL = f'{URL_BASE}:{PORT}'


class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(HTTPStatus.OK)
        self.send_header('Content-type','text/html')
        self.end_headers()

        message = "Too hot"
        self.wfile.write(bytes(message, "utf8"))

    def do_POST(self):
        self.send_response(HTTPStatus.OK)
        self.send_header('Content-type','text/html')
        self.end_headers()

        message = "Hello, World! Here is a POST response"
        self.wfile.write(bytes(message, "utf8"))
