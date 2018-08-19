# coding: utf-8
import time

import requests
import pandas as pd





headers = {
    'cookie': 'd_c0="ACDCPmdICwuPTigEug6pEl3I4k10mZe_UhQ=|1482515738"; _zap=e798a229-490c-4cde-91ea-36b89e6681d8; aliyungf_tc=AQAAALPVxzxtVgQABwlne6k5DCmEySdD; _xsrf=d735e70c22d6e3c2668ba82291b5be45; s-t=autocomplete; _ga=GA1.2.1857950206.1486515046; acw_tc=AQAAADiGa1zg8QsA/QUjfUtUeBAKm0st; acw_tc=59bcd520|d289569532f6ff2c7efb8b4a697768ee; q_c1=2e7d9ee39a7c44b8973a6d098136847f|1507049573000|1485875549000; s-q=%E9%82%AA%E6%81%B6%E5%8A%9B%E9%87%8F; s-i=1; sid=44kpke6g; _xsrf=d735e70c22d6e3c2668ba82291b5be45; __DAYU_PP=6yYeR2rQavuQaEq6rbNQ251d9adf4d31; capsion_ticket="2|1:0|10:1534232454|14:capsion_ticket|44:NDg4OTMxMmYwODc3NDZhMWE3YmIzZWUzMzMzODFlMjY=|1710c8b10c25d234ad49a3bde6fd440bcd275df2dd7bb12e51c73630d365e385"; z_c0="2|1:0|10:1534232455|4:z_c0|92:Mi4xNTk4WEFBQUFBQUFBSU1JLVowZ0xDeVlBQUFCZ0FsVk5oOVZmWEFDSjZkNlJkNmdBLTdOLWpTTEJ1US1ZcFF4akhR|ef0ec3b266687b1d326e52494213db3ee04da31144a5e04614c674024f199bcc"; q_c1=2e7d9ee39a7c44b8973a6d098136847f|1534232455000|1485875549000; __utma=51854390.1857950206.1486515046.1534232466.1534232466.1; __utmc=51854390; __utmz=51854390.1534232466.1.1.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmv=51854390.100-1|2=registration_date=20130918=1^3=entry_date=20130918=1; tgw_l7_route=931b604f0432b1e60014973b6cd4c7bc',
    # x-udid: ACDCPmdICwuPTigEug6pEl3I4k10mZe_UhQ=
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
}

user_data = []

def get_user_data(page):
    for i in range(page):
        url = 'https://www.zhihu.com/api/v4/members/excited-vczh/followees?include=data%5B*%5D.answer_count%' \
              '2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F' \
              '(type%3Dbest_answerer)%5D.topics&offset={}&limit=20'.format(i*20)
        response = requests.get(url=url, headers=headers).json()['data']
        user_data.extend(response)
        print("正在爬去第{0}页".format(i))
        time.sleep(1)

# df = pd.DataFrame.from_dict(response)
# print(df.head())
# df.to_csv('zhihu.csv')


if __name__ == '__main__':
    get_user_data(10)
    df = pd.DataFrame.from_dict(user_data)
    df.to_csv('zhihu.csv',encoding='utf-8')