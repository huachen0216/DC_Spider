# coding: utf-8
import requests
from lxml import etree

# 豆瓣《小王子》短评
# url = 'https://book.douban.com/subject/1084336/comments/'
# r = requests.get(url).text
# s = etree.HTML(r)
# print(s.xpath('//*[@id="comments"]/ul/li[8]/div[2]/p/text()'))
# print(s.xpath('//div[@class="comment"]/p/span/text()'))

# 知乎话题精华
# url = 'https://www.zhihu.com/topic/19552832/top-answers'
# r = requests.get(url=url).text
# print(r)


# 小猪短租
url = 'http://bj.xiaozhu.com'
r = requests.get(url=url).text
# print (r)

s = etree.HTML(r)
print(s.xpath('//*[@id="page_list"]/ul/li[3]/div[2]/div/a/span/text()'))
