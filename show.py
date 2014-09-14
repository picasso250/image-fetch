#!/usr/bin/env python
# -*- coding: utf-8 -*-

import http.server

def run(server_class=http.server.HTTPServer, handler_class=BaseHTTPRequestHandler):
    server_address = ('', 8080)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

class MyHanlder(http.server.BaseHTTPRequestHandler):
    """docstring for MyServer"""
    def __init__(self):
        super(MyHanlder, self).__init__()
    def do_GET():
        pass
        
run()
