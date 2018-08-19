# _*_ coding: utf-8 -*-

import os
import urllib.request
from bs4 import BeautifulSoup

root_url = 'http://iyangzi.com/?p=239'
try:
    response = urllib.request.urlopen(root_url)
    if response.status == 200:
        girl_dir = "C:\\Users\\jidi\\Desktop\\girl"
        if not os.path.exists(girl_dir):
            os.mkdir(girl_dir)
        os.chdir(girl_dir)
        soup = BeautifulSoup(response.read(), 'html.parser', from_encoding='utf-8')
        all_img = soup.find('div', class_='post-content').find_all('img')
        count = 1
        for img in all_img:
            src = img['src']
            print(src)
            name = 'iyangzi' + str(count)
            with open(name + '.jpg', 'ab') as img_object:
                img_content = urllib.request.urlopen(src).read()
                img_object.write(img_content)
                img_object.flush()
            count += 1
except urllib.error.HttpError as e:
    print(e)