#!/usr/bin/env python

from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler

class RequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write('%s %s %s\n' % (self.command, self.path, self.request_version))
        self.wfile.write(self.headers)
        self.finish()
        self.connection.close()

port = 8000
server = HTTPServer(('', port), RequestHandler)
server.serve_forever()