# -*- coding:utf-8 -*-
import requests
from lxml import etree
import pandas as pd

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"}
lista =[]
for idx in range(0,250,25):
    url = f'https://movie.douban.com/top250?start=0&filter='
    r = requests.get(url,headers=header)
    et = etree.HTML(r.text)
    items = et.xpath('//div[@class="item"]')
    datas=[]
    for item in items:
        # xpath 得到的都是列表，注意取值
        rank = item.xpath('.//em[@class=""]/text()')# ./表示当前item元素开始找，一定记得
        title = item.xpath('.//div[@class="hd"]//span[@class="title"]/text()')
        star = item.xpath('.//div[@class="star"]//span/@class')
        rating_num = item.xpath('.//div[@class="star"]//span[@class="rating_num"]/text()')
        comment = item.xpath('.//div[@class="star"]//span')[3].xpath('./text()')[0][:-3]
        datas.append({'rank':rank[0],
                      "title":title[0],
                      "star":star[0],
                      "comment":comment})
    lista.extend(datas)
df = pd.DataFrame(lista)
print(df.head())


