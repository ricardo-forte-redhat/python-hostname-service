#!/usr/bin/env python

import textwrap, os

from six.moves.BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer


class HelloRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

        response_text = "Python-"

        response_text = response_text + os.environ.get('HOSTNAME')
          
        self.wfile.write(response_text.encode('utf-8'))


server_address = ('', 8080)
httpd = HTTPServer(server_address, HelloRequestHandler)
httpd.serve_forever()