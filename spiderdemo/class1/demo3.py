import os
from os import path

import pandas
import requests
from bs4 import BeautifulSoup

comments = []
r = requests.get('https://book.douban.com/subject/1084336/comments/').text
# print(r)

soup = BeautifulSoup(r,'lxml')
pattern = soup.find_all('p', 'comment-content')
for item in pattern:
    # print(item.contents[1].contents[0])
    comments.append(item.contents[1].contents[0])
    # comments.append(item.string)
#print(comments)


csv_path = path.dirname(path.abspath(__file__))
df = pandas.DataFrame(comments)
df.to_csv(csv_path+'/comments.csv')