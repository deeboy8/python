import socketserver
import http.server 
import urllib

PORT = 4000

class myproxy(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        url = self.path[1:]
        self.send_response(200)
        self.end_headers()
        self.copyfile(urllib.urlopen(url), self.wfile)

def main():
    # global PORT = 4000
    server = HTTPServer(('localhost', PORT), myproxy)
    print('Server running on port %s' %PORT)
    httpd = socketserver.ForkingTCPServer(('', PORT), myproxy)
    httpd.serve_forever()

if __name__ == '__main__':
    main()