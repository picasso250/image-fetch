#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import kv
import webbrowser

tag_list = []
attitude = kv.get('attitude')
print(attitude)
root = 'images'
files = os.listdir(root)
for name in files:
    f = root+'/'+name
    if attitude.get(f) == 'l':
        tag_list.append('<img src="'+f+'">')

print(tag_list)
html = '\n'.join(tag_list)
print(html)

show_file = 'show.html'
f = open(show_file, 'w')
f.write(html)
f.close()

url = 'file://'+os.getcwd()+'/'+show_file
print(url)
webbrowser.open(url)
