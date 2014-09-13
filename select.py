#!/usr/bin/env python
# -*- coding: utf-8 -*-

# apt-get install python3-tk
# pip-3.2 install Pillow
# apt-get install python3-pil
# sudo apt-get install python3-pil.imagetk

import os
import webbrowser
from PIL import Image
import kv

kv_data = kv.get()
root = 'images'
files = os.listdir(root)
# print(files)
for f in files:
    f = root+'/'+f
    if f in kv_data:
        print('u',kv_data[f],f)
        continue
    if not os.path.isfile(f):
        print('warning', f, 'is not file')
        continue
    img = Image.open(f)
    try:
        img.show()
    except IOError as e:
        print('IOError')
    else:
        pass
    finally:
        pass
    prompt = 'Like this image '+f+'? [Like/Delete/Pass/Open/LikeAll] '
    page_key = 'page of '+f
    can_open = page_key in kv_data

    while True:
        action = input(prompt)
        kv_data[f] = action
        if action == 'd':
            print('delete', f)
            os.remove(f)

        if action == 'o':
            if can_open:
                webbrowser.open(kv_data[page_key])
        else:
            break

    kv.save(kv_data)
