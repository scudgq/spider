import requests
from urlmanager import url_manager
import re
from bs4 import BeautifulSoup

root_url = 'https://www.crazyant.net/'
urls = url_manager.UrlManager
urls.add_new_url(root_url)
fout = open('爬取蚂蚁博客文章.txt', 'w')
while urls.has_new_url():
    curr_url = urls.get_url()
    r = requests.get(curr_url,timeout=5)
    if r.status_code != 200:
        print('current url status_code is not 200',curr_url)
        continue
    soup = BeautifulSoup(r.text,'html.parser')
    title = soup.title.string
    fout.write(f"{curr_url} ,{title}\n")
    fout.flush()
    print(f"{curr_url},{title}")
    links = soup.find_all('a')
    for link in links:
        href = link.get('href')
        if href is None:
            continue
        obj = r"^https://www.crazyant.net/\d+.html$"
        if re.match(obj,href):
            urls.add_new_url(href)

fout.close()



