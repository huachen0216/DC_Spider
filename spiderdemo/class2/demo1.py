import requests

r = requests.get('https://book.douban.com/subject/1084336/comments')
print(r.apparent_encoding)
print(r.text)
