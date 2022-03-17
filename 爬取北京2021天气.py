# -*- coding:utf-8 -*-
import requests
import re
import pandas as pd
listall = []
for idx in range(1,13):
    url = f'https://tianqi.2345.com/Pc/GetHistory?areaInfo[areaId]=54511&areaInfo[areaType]=2&date[year]=2021&date[month]={idx}'

    r = requests.get(url)
    res = r.json()#爬取到的是json数据可以用这个方式处理为text
    data = res['data']
    obj = re.compile(r'<td>(?P<date>.*?)</td>.*?<td.*?">(?P<HT>.*?)</td>.*?<td.*?" >(?P<LP>.*?)</td>'
                         '.*?<td>(?P<tianqiinfo>.*?)</td>.*?<td>(?P<fenglifengxiang>.*?)</td>.*?<td>.*?">'
                     '(?P<tianqizhishu>.*?)</span></td>',re.S)
    results = obj.finditer(data)
    lista =[]
    for result in results:
        item = result.groupdict()#groupdict 方便处理数据
        lista.append(item)#所有字典放到一个列表
    listall.extend(lista)
df = pd.DataFrame(listall)#列表DATAFRAME
df.set_index('date',inplace=True)#设置index
df.to_excel('北京2021天气.xlsx')#记得加上.xlsx



