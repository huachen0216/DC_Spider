# coding: utf-8

import sqlite3

import requests
from bs4 import BeautifulSoup




class QDaily_DB():

    def __init__(self):
        self.conn=None

    def create_db(self):
        self.conn=sqlite3.connect('qdaily.db')
        self.conn.execute("""
              create table if not exists qdaily(
              id INTEGER PRIMARY KEY ,
              title varchar DEFAULT NULL ,
              sharenum int DEFAULT NULL ,
              data DATE DEFAULT NULL ,
              comments_num int DEFAULT NULL )""")

        self.conn.execute("""
                      create table if not exists comments(
                      id INTEGER PRIMARY KEY ,
                      url_id int DEFAULT NULL ,
                      comment varchar DEFAULT null )""")

        self.conn.close()

class Spider():

    def __init__(self):
        self.url_base = "http://www.qdaily.com/articles/"

    def html_download(self,id=1):
        qdaily_pri_data=[]
        qdaily_cmt_data=[]
        print('爬取第{}个网页'.format(id))
        real_url = self.url_base+str(id)+".html"
        try:
            response = requests.get(real_url, timeout=10)
            response.encoding = response.apparent_encoding
            html_content = response.text
            if "网页出错" in html_content:
                return
            qdaily_pri_data,qdaily_cmt_data=self.parse_html(html_content,real_url,id)
        except Exception as e:
            print('parse id :{} failed:{}'.format(id,e))
        finally:
            return qdaily_pri_data,qdaily_cmt_data

        soup = BeautifulSoup(html_content, "html.parser")
        sharmnum = int(soup.find('span', 'num').string)
        title = soup.find('h2', 'title').string
        date = soup.find('span', 'date smart-date').attrs['data-origindate'][:-15]

        comment_url = "http://www.qdaily.com/comments/article/" + str(id) + "/0.json"
        comment_response = requests.get(comment_url, headers=head, timeout=10).text
        json_dict = json.loads(comment_response)
        comments_data = json_dict['data']['feeds']
        comments = json_dict['data']['total_count']
        primary_data = (id, title, sharmnum, date, comments)
        json_dict = json.loads(comment_response)




