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

attitude = kv.get('attitude')
root = 'images'
files = os.listdir(root)
# print(files)
for f in files:
    f = root+'/'+f
    if f in attitude:
        print('u',attitude[f],f)
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
    prompt = 'Like image '+f+'? [Pass/Like/Delete] '
    image_page = kv.get('image_page')
    can_open = f in image_page
    if can_open:
        prompt = 'Like image '+f+'? [Pass/Like/Delete/Open/LikeAll/DeleteAll] '
        page_url = image_page[f]

    while True:
        action = input(prompt)
        if action == '':
            print('default is Pass')
            action = 'p'
        attitude[f] = action
        if action == 'd':
            print('delete', f)
            os.remove(f)
        if action == 'la' or action == 'da':
            if can_open:
                action = action[0]
                page_images = kv.get('page_images')
                images = page_images[page_url]
                for image in images:
                    print(action, image)
                    attitude[image] = action
            else:
                print('error, can not do to all')

        if action == 'o':
            if can_open:
                webbrowser.open(page_url)
            else:
                print('error, can not open')
        else:
            break

    kv.save('attitude', attitude)
