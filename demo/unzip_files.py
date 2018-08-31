#! /usr/bin/env python
# -*- coding:utf-8 -*-

import subprocess
import os


list = subprocess.Popen('ls *.zip', shell=True, stdout=subprocess.PIPE).stdout.read()
# print(str(list, 'utf8'))

new_list = (str(list,'utf8')).split('\n')
new_list1 = []

for item in new_list:
    if (item != '' and item.index("zip") > 0 ):
        new_list1.append(item)


# print(new_list1)

for file in new_list1:
    print(file)
    command = "/usr/bin/unzip -O CP939 "+file
    subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)

