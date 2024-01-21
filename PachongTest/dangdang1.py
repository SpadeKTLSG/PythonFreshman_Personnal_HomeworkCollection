import re
import time
import requests
from lxml import etree
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import pandas as pd
# from Chap5_MySQLLoader import MySQLLoader
import numpy as np
from pandas.plotting import register_matplotlib_converters
import numpy as np
import matplotlib.dates as mdates
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from datetime import datetime


class DangDang:
    def __init__(self,year):
        self.url = "http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-year-{}-0-1-".format(year)
        self.ua = UserAgent(verify_ssl=False)
        self.headers = {
            "Cookie": "s_ViewType=10; _lxsdk_cuid=167ca93f5c2c8-0c73da94a9dd08-68151275-1fa400-167ca93f5c2c8; _lxsdk=167ca93f5c2c8-0c73da94a9dd08-68151275-1fa400-167ca93f5c2c8; _hc.v=232064fb-c9a6-d4e0-cc6b-d6303e5eed9b.1545291954; cy=16; cye=wuhan; td_cookie=686763714; _lxsdk_s=%7C%7CNaN",
            "User-Agent": self.ua.random  # 获取随机的User-Agent
        }
        self.dic = {}  # class-digit字典
        self.rank_list = []
        self.name_list = []
        self.comment_list = []
        self.publish_date_list = []
        self.publisher_list = []
        self.price_discount_list = []
        self.price_original_list = []
        return

    def get_page(self, page):

        url = "{}{}".format(self.url, page)
        res = requests.get(url, headers=self.headers)
        # print(res.text)

        soup = BeautifulSoup(res.text, 'html.parser')
        tag = soup.find('ul', 'bang_list_mode')

        li_list = tag.find_all('li')
        # print(li_list[1])

        for item in li_list:
            # 排名
            rank = item.find('div', 'list_num')
            # print(rank.string)
            self.rank_list.append(rank.string.replace('.', ''))

            # 书名
            name = item.find('div', 'name')
            # print(name.w['title'])
            self.name_list.append(name.w['title'])

            # 评论
            comment = item.find('div', 'star')
            # print(comment.w.string)
            self.comment_list.append(comment.w.string.replace('条评论', ''))

            # 出版日期
            publish = item.find_all('div', 'publisher_info')
            # print(publish[1].span.string)
            self.publish_date_list.append(publish[1].span.string)

            # 出版社
            # print(publish[1].w.string)
            self.publisher_list.append(publish[1].w.string)

            # 折扣价
            price_discount = item.find('span', 'price_n')
            # print(price_discount.string)
            self.price_discount_list.append(price_discount.string.replace('¥', ''))

            # 原价
            price_original = item.find('span', 'price_r')
            # print(price_original.string)
            self.price_original_list.append(price_original.string.replace('¥', ''))

    # def to_db(self, filename, tablename, dbinfo):
    #     loader = MySQLLoader(filename, 'csv', tablename, dbinfo)
    #     loader.load()

    def to_csv(self, filename):
        df = pd.DataFrame({
            'rank': pd.Series(self.rank_list),
            'name': pd.Series(self.name_list),
            'comment': pd.Series(self.comment_list),
            'publish_date': pd.Series(self.publish_date_list),
            'publisher': pd.Series(self.publisher_list),
            'price_discount': pd.Series(self.price_discount_list),
            'price_original': pd.Series(self.price_original_list)
        })

        df.to_csv(filename, index=False, encoding='utf-8-sig')
        return df


if __name__ == '__main__':
    dp = DangDang(2021)
    for page in range(1, 6):
        dp.get_page(page)
    df = dp.to_csv('chap7.csv')

    # db_info = {
    #     'host': 'MySQL数据库服务器地址',
    #     'port': 3306,
    #     'user1': '数据库用户名',
    #     'password': '数据库密码',
    #     'database': '数据库名称'
    # }

    # 爬取畅销榜并入库
    #  dp.to_db('chap7.csv', 'tb_dd_rank', db_info)

    # 评论数最多、出版日期最新、折扣最低
    df = pd.read_csv('chap7.csv', sep=',')

    # 评论数最多
    df['comment'] = df['comment'].astype('int')
    comment_list = df.copy().sort_values(by='comment', ascending=False)[:1]
    print(comment_list)

    # 出版日期最新
    publish_date_list = df.copy().sort_values(by='publish_date', ascending=False)[:1]
    print(publish_date_list)

    # 折扣最低
    df['price_discount'] = df['price_discount'].astype('float32')
    df['price_original'] = df['price_original'].astype('float32')
    df['discount_rate'] = df['price_discount'] / df['price_original']
    discount_rate_list = df.copy().sort_values(by='discount_rate', ascending=True)[:1]
    print(discount_rate_list)

    register_matplotlib_converters()
    plt.figure(figsize=(20, 15))

    book_list = pd.read_csv('chap7.csv', sep=',')
    book_list['discount_rate'] = book_list['price_discount'] / book_list['price_original']

    x = book_list['rank']
    ax1 = plt.subplot(221)
    y1 = book_list['comment']
    ax1.plot(x, y1, 'bD-')

    ax2 = plt.subplot(222)
    y2 = book_list['price_discount']
    y3 = book_list['price_original']
    ax2.plot(x, y2, 'r^-')
    ax2.plot(x, y3, 'gH-')

    ax3 = plt.subplot(223)
    y4 = (book_list['discount_rate'] * 100).round(1)
    ax3.plot(x, y4, 'ks-')

    ax4 = plt.subplot(224)
    y5 = [datetime.strptime(d, '%Y-%m-%cart').date() for d in book_list['publish_date']]
    ax4.plot(x, y5, 'm4-')

    plt.show()
