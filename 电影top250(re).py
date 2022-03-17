import requests
import re
import pandas as pd
'''
obj =re.compile(r'',re.S)
result = obj.finditer(r.text)
'''
header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
}
listall=[]
for idx in range(0,250,25):
    url = f'https://movie.douban.com/top250?start={idx}&filter='
    lista =[]
    r = requests.get(url,headers = header)
    r.encoding ='utf-8'
    obj = re.compile(r'.*?<em class="">(?P<rank>.*?)</em>.*?<span class="title">(?P<title>.*?)</span>.*?v:average">(' \
          r'?P<ratings>.*?)</span>.*?</span>'r'.*?<span>(?P<pepoles>.*?)</span>',re.S)

    result = obj.finditer(r.text)
    for item in result:
        data = item.groupdict()

        lista.append(data)
    listall.extend(lista)
df = pd.DataFrame(listall)
print(df.head())

