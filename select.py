#!/usr/bin/env python
# -*- coding: utf-8 -*-

# apt-get install python3-tk
# pip-3.2 install Pillow
# apt-get install python3-pil
# sudo apt-get install python3-pil.imagetk

import os
from PIL import Image
import attitude

file_table = attitude.get()
root = 'images'
files = os.listdir(root)
# print(files)
for f in files:
    f = root+'/'+f
    if not os.path.isfile(f):
        print('warning', f, 'is not file')
        continue
    img = Image.open(f)
    img.show();
    action = input('Like this image? [Like/Delete/Pass] ')
    file_table[f] = action

    attitude.save(file_table)
