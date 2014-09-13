#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, re
import urllib.request
import urllib.parse

class AppURLopener(urllib.request.FancyURLopener):
    version = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.94 Safari/537.36'

urllib._urlopener = AppURLopener()

def image_save(name, url):
    if os.path.isfile(name):
        return False
    content = fetch_url(url)
    f = open(name, 'w')
    f.write(content)
    f.close()

def fetch_url(url):
    response = urllib.request.urlopen(url) 
    page = response.read()
    return page

# fetch_url('http://www.douban.com/group/asshole/?ref=sidebar')
def fetch_page(page_url):
    html = fetch_url(page_url)
    html = html.decode()
    print( html)
    match = re.findall(r'<img src="([^"]+.douban.com/view/group_topic/large/public/p\d+\.jpg)"', html)
    if match is None:
        print( "no image in this page\n")
        return False
    for image_url in match:
        file_name = image_url[image_url.rfind('/')+1:]
        file_name = 'images/'+file_name
        if os.path.isfile(file_name):
            print( "skip file_name\n")
            continue
        print( "save",file_name)
        urllib.request.urlretrieve(image_url, file_name)

group_root = 'http://www.douban.com/group/haixiuzu/';
html = fetch_url(group_root);
html = html.decode()
print( html)
matches = re.findall('<a href="(http://www.douban.com/group/topic/\d+/)"', html)
if matches is None:
    raise Exception("no link for group topic")
for topic_url in matches:
    print(topic_url)
    print( "fetch topic", topic_url)
    fetch_page(topic_url);