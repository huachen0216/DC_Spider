# coding: utf-8
import requests
from lxml import etree
import openpyxl
import xlwt

import pandas as pd
import numpy as np

url = 'https://book.douban.com/subject/1084336/comments/'
r = requests.get(url=url).text

s = etree.HTML(r)
file = s.xpath('//div[@class="comment"]/p/span/text()')
# print (file)

# open方法存文件
# with open('pinglun.txt', 'a', encoding='utf-8') as f:
#     for i in file:
#         print(i)
#         f.write(i+'\n')


# pandas方法存文件
df = pd.DataFrame(file)
# print(df.head())

# df.to_csv('pandas.csv')

df.to_excel('pandas.xlsx')