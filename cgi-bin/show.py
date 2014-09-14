#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import kv

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

for f in files:
    file_path = image_root+'/'+f
    image_key = 'images/'+f
    image_url = '/'+image_key
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

