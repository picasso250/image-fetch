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
for f in attitude:
    if len(attitude[f]) > 1:
        print(attitude[f],'==>',attitude[f][0])
        attitude[f] = attitude[f][0]
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
    try:
        img = Image.open(f)
        img.show()
    except OSError as e:
        print('OSError')
        attitude[f] = 'd'
        continue
    except IOError as e:
        print('IOError')
        attitude[f] = 'd'
        continue
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
                    if image not in attitude:
                        print(action, image)
                        attitude[image] = action
                    else:
                        print('u already',attitude[image],image)
            else:
                print('error, can not do to all')
                continue

        if action == 'o':
            if can_open:
                webbrowser.open(page_url)
            else:
                print('error, can not open')
        else:
            break

    kv.save('attitude', attitude)
