# -*- coding: utf-8 -*-

import os
import json

def get(table = 'info'):
    info_file = table+'.json'
    if os.path.isfile(info_file):
        f = open(info_file, 'r')
        file_table = json.load(f)
        f.close()
    else:
        file_table = {}
    return file_table

def save(table, data):
    info_file = table+'.json'
    f = open(info_file, 'w')
    json.dump(data, f)
    f.close()
