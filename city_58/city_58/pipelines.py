# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json

from pymongo import MongoClient

client = MongoClient()
db = client.city_58
data= db.data

class City58Pipeline(object):

    def open_spider(self, spider):
        # self.file = open('58_zufang.txt', 'w', encoding='utf-8')
        print('start spider...')

    def process_item(self, item, spider):
        # line = json.dumps(dict(item))
        line = dict(item)
        # self.file.write(line)
        data.insert(line)
        return item

    def close_spider(self, spider):
        self.file.close()
        print('end spider...')