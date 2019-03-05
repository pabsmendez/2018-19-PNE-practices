import http.server
import socketserver

PORT = 8090


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        print("GET received")

        print("Request line:" + self.requestline)
        print("  Cmd: " + self.command)
        print("  Path: " + self.path)

        if "/" == self.path:
            f = open("indexP5.html", "r")
            content = f.read()
            f.close()

        elif "blue" in self.path:
            f = open("blueP5.html", "r")
            content = f.read()
            f.close()

        elif "pink" in self.path:
            f = open("pinkP5.html", "r")
            content = f.read()

        elif "green" in self.path:
            f = open("greenP5.html", "r")
            content = f.read()

        else:
            f = open("error.html")
            content = f.read()
            f.close()

        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.send_header('content_Lenght', len(str.encode(content)))
        self.end_headers()

        self.wfile.write(str.encode(content))

        return


Handler = TestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at PORT", PORT)

    httpd.serve_forever()