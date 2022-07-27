from http.server import HTTPServer
from src.http_server.http_server import URL_BASE, PORT, Handler

with HTTPServer((URL_BASE, PORT), Handler) as server:
    server.serve_forever()
