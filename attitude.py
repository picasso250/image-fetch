# -*- coding: utf-8 -*-

import os
import json

info_file = 'info.json'

def get():
    if os.path.isfile(info_file):
        f = open(info_file, 'r')
        file_table = json.load(f)
        f.close()
    else:
        file_table = {}
    return file_table

def save(file_table):
    f = open(info_file, 'w')
    json.dump(file_table, f)
    f.close()
