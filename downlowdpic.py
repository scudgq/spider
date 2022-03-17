# -*- coding:utf-8 -*-
import requests
import re
import os

url1 = 'https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js?ts=2745716'
headers ={
"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"
}
r = requests.get(url1,headers=headers).json()
# print(r)
heros = r['hero']
number ,pic= 1,0
for hero in heros:
    heroid = hero['heroId']
    name = hero['name']
    number+=1
    print((heroid,name))
    if not os.path.exists(f'D:\pictcures'):
        os.mkdir(f'D:\pictcures')
    url =f'https://game.gtimg.cn/images/lol/act/img/js/hero/{heroid}.js?ts=2745715'
    res = requests.get(url,headers=headers)
    res.encoding='gbk'
    data_all = res.json()
    datas = data_all['skins']
    pattern =r'https://game.gtimg.cn/images/lol/act/img/skin/big\d+.jpg'
    data = str(datas)
    results = re.findall(pattern,data)#content 只能是字符串
    idx = len(results)
    for result in results:
        res = requests.get(result,headers=headers)
        img_name = result.split('/')[-1]
        with open(f'D:\pictcures\{name}_{img_name}','wb') as f:
            f.write(res.content)
            pic+=1
            print(f'{name}_{img_name}下载完毕')
print(number,pic)

