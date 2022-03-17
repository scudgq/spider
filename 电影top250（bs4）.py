import requests
from bs4 import BeautifulSoup
import pandas as pd

header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
}
lista=[]
for idx in range(0,250,25):
    url = f'https://movie.douban.com/top250?start={idx}&filter='
    r = requests.get(url,headers= header)
    r.encoding = 'utf-8'
    soup = BeautifulSoup(r.text,'html.parser')
    items = soup.find("ol",  class_="grid_view").find_all('div',class_="item")
    data=[]
    for item in items:
        rank  = item.find('em').get_text()
        title = item.find("div" ,class_="info").find("span" ,class_="title").get_text()
        result =item.find("div" ,class_="info").find("div" ,class_="bd").find("div", class_="star")
        rating_num = result.find("span",class_="rating_num").get_text()
        comment = result.find_all('span')[3].get_text()[:-3]
        data.append({'rank':rank,
                    'title':title,
                    'rating_num':rating_num,
                    "comment":comment})
    lista.extend(data)
df = pd.DataFrame(lista)
df.to_excel('bs4-top250电影.xlsx',index= False)




