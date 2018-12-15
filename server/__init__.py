from http.server import BaseHTTPRequestHandler, HTTPServer

app = []

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<h1>Hello world!</h1>", "utf-8"))
        self.wfile.write(bytes("<hr>", "utf-8"))
        self.wfile.write(bytes("<p>You accessed path: %s</p>" % self.path, "utf-8"))


def run():
    global app
    host = app.config.host
    port = int(app.config.port)
    server = HTTPServer((host, port), MyServer)
    print('Server starts - %s %s' % (host, port))
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass

    server.server_close()
    print('Server Stops - %s %s' % (host, port))
