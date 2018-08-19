# coding: utf-8

# pretend brower
import json
import re

import requests

headers = {
    'User-Agent':   'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36 ',
    'Accept':   'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,ja;q=0.7,zh-TW;q=0.6,en-US;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
}

url = "https://itunes.apple.com/cn/app/id414478124"

html = requests.get(url, headers=headers)
data = html.text

real_name_reg = ' <h1 class="product-header__title">(.*?)<span class="badge badge--product-title">'
real_name = re.compile(real_name_reg, re.S).findall(data)

rating_star_reg = '<span class="we-customer-ratings__averages__display">(.*?)<'
rating_star = re.compile(rating_star_reg, re.S).findall(data)

history_reg = '<li class="version-history__item">.*?</li>'
history_versions = re.compile(history_reg, re.S).findall(data)

info_dict = dict()
history_list = list()

for each_version in history_versions:
    history_info_dict = dict()

    version_reg = '<h4 class="version-history__item__version-number">.*?</h4>'
    update_datetime_reg = 'datetime="(.*?)" id='
    description_reg = '<div title="(.*?)"'

    result_version = re.compile(version_reg, re.S).findall(data)
    result_update_datetime = re.compile(update_datetime_reg, re.S).findall(data)
    result_description = re.compile(description_reg, re.S).findall(data)

    history_info_dict["version"] = result_version[0].strip()
    history_info_dict["datetime"] = result_update_datetime[0].strip()
    history_info_dict["description"] = result_description[0].strip()

    history_list.append(history_info_dict)


info_dict["name"] = real_name[0].strip()
info_dict["rating_star"] = rating_star[0].strip()
info_dict["history_list"] = history_list

info_json = json.dumps(obj=info_dict, ensure_ascii=False, indent=4, separators=(',',':'),sort_keys=True)

with open(real_name[0].strip() + "_info.json", "w+") as file:
    file.write(info_json)






