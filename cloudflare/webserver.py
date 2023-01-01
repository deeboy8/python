from http.server import HTTPServer, BaseHTTPRequestHandler

# class server(BaseHTTPRequestHandler):
#     # method runs when receive a get request
#     # get request = request by client to server
#     def do_GET(self):
#         if self.path == '/':
#             self.path = 'index.html'
#         try:
#             file_to_open = open(self.path[1:]).read()
#             self.send_response(200)
#         except:
#             file_to_open = "File not found"
#             self.send_response(404)
#         self.end_headers() #required by BaseHTTPRequestHandler response handler class
#         self.wfile.write(bytes(file_to_open, 'utf-8'))

# httpd = HTTPServer(('localhost', 8000), server)
# httpd.serve_forever()

class helloHandler(BaseHTTPRequestHandler):
    #handles how we respond to GET requests
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        self.wfile.write("Hello Demitrus!".encode())

def main():
    PORT = 8000
    server = HTTPServer(('localhost', PORT), helloHandler)
    print('Server running on port %s' %PORT)
    server.serve_forever()

if __name__ == '__main__':
    main()
