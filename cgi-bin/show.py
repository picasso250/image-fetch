#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# python3 -m http.server --cgi 8000

import os, time
import cgi
from urllib.parse import parse_qs
import operator
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
log.debug('is_all', str(is_all))

file_time_list = [(f, image_root+'/'+f, os.path.getmtime(image_root+'/'+f)) for f in files]
if is_all:
    file_time_list = sorted(file_time_list, key=operator.itemgetter(2), reverse=True)
else:
    file_time_list = [x for x in file_time_list if time.time() - x[2] < 3600*24]

last_date = None
for f, file_path, mtime in file_time_list:
    image_key = 'images/'+f
    image_url = '/'+image_key

    this_date = time.strftime('%Y-%m-%d', time.gmtime(mtime))
    if last_date is None or last_date != this_date:
        last_date = this_date
        print('<h1>', this_date, '</h1>')

    if os.path.isfile(file_path):
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

