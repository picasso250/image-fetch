#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# python3 -m http.server --cgi 8000

import os, time
import cgi
from urllib.parse import parse_qs
import kv
import log

# enable debugging
import cgitb
cgitb.enable()

print("Content-Type: text/html;charset=utf-8\r")
print("\r")

root = os.getcwd()

f = open(root+'/head.html')
print(f.read())
f.close()

image_root = root+'/images'
files = os.listdir(image_root)
image_page = kv.get('image_page')
attitude = kv.get('attitude')
get = cgi.FieldStorage()
QUERY_STRING = os.environ["QUERY_STRING"]
log.debug('QUERY_STRING', QUERY_STRING)
get = parse_qs(QUERY_STRING, True)
log.debug(str(parse_qs(QUERY_STRING, True)))
is_all = 'all' in get

for f in files:
    file_path = image_root+'/'+f
    image_key = 'images/'+f
    image_url = '/'+image_key
    mtime = os.path.getmtime(file_path)
    # print(mtime)
    is_today = time.time() - mtime < 3600*24
    # print(is_today)

    log.debug('is_all', str(is_all))
    log.debug('is_all or is_today',str(is_all or is_today))

    if os.path.isfile(file_path) and (is_all or is_today):
        entry_html = '''<div class="entry">
    <img src='%s'>
    <div>
        <span class="btn btn-like" data-file="%s" data-action="like">like</span>
        <span class="btn btn-delete" data-file="%s" data-action="delete">delete</span>
        ''' % (image_url,image_key,image_key)
        if image_key in image_page:
            entry_html += '<a href="%s" target="_blank">link</a>'%image_page[image_key]
        entry_html += '</div> </div>'
        print(entry_html)

