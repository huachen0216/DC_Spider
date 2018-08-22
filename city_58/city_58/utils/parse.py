# coding: utf-8
from pyquery import PyQuery
from scrapy import Selector

with open('index.html', encoding='utf-8') as f:
    text = f.read()


# print(text)

# sel = Selector(text=text)
# pass

jpy = PyQuery(text)

items = jpy('li')

for item in items.items():
    print(item.text())
    print(item.attr('class'))