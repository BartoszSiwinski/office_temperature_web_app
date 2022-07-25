from http.server import BaseHTTPRequestHandler, HTTPServer

LOCALHOST_URL = 'http://localhost:8000/'


class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        print(self.requestline)
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

        message = "Too hot"
        self.wfile.write(bytes(message, "utf8"))

    # def do_POST(self):
    #     self.send_response(200)
    #     self.send_header('Content-type','text/html')
    #     self.end_headers()
    #
    #     message = "Hello, World! Here is a POST response"
    #     self.wfile.write(bytes(message, "utf8"))


with HTTPServer(('localhost', 8000), Handler) as server:
    server.serve_forever()


# class Handler(BaseRequestHandler):
#
#     def handle(self):
#         print("Got connection from", self.client_address)
#         print("Request:", self.request)
#         while True:
#             msg = self.request.recv(8192)
#             if not msg:
#                 break
#             self.request.send(msg)
#
#
# if __name__ == '__main__':
#     server = TCPServer(('', 8000), Handler)
#     server.serve_forever()
