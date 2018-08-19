import urllib

f = urllib.request.urlopen('http://www.baidu.com')
# f.read(500)
print (f.read())
# f.read(500).decode('utf-8')
print(f.read().decode('utf-8'))
