#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os
import kv
import cgi
import json
import log

# enable debugging
import cgitb
cgitb.enable()

print("Content-Type: application/json;charset=utf-8\r")
print("\r")

root = os.getcwd()

attitude_map = kv.get('attitude')

post = cgi.FieldStorage()

action = post['action'].value
action = action[0]
f = post['file'].value
attitude_map[f] = action
file_path = root+'/'+f
if action == 'd' and os.path.isfile(file_path):
    os.remove(file_path)
kv.save('attitude', attitude_map)
print(json.dumps({'code': 0, 'action':action, 'file': f}));
