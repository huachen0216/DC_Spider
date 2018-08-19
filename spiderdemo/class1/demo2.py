import requests

r = requests.get('https://www.class1.com/')
print(r)
# r.text
print(r.text)
r.encoding='utf-8'
# r.text
print(r.text)