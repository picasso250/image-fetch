# -*- coding: UTF-8 -*-

import time

def debug(*args):
    f = open('/tmp/douban-image.log', 'a')
    f.write('debug '+time.strftime('%Y-%m-%d %H:%M:%S ')+' '.join(args)+'\n')
    f.close()
