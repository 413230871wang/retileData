import requests
import re
from bs4 import BeautifulSoup

# 网页的请求头
header = {
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
}

# url链接
url = 'http://guide.medlive.cn/guideline/18989'
response = requests.get(url, headers=header)

# 通过BeautifulSoup进行解析出每个房源详细列表并进行打印
soup = BeautifulSoup(response.text, 'html.parser')
result_h1 = soup.find_all('h1',{'class':'text_title'})
print(result_h1[0].text)
result_div = soup.find_all('div',{'class' : 'one_info clearfix'})
soup_p = BeautifulSoup(str(result_div),'lxml')
result_p = soup_p.find_all('p')
print(result_p[1].text)
for i in result_p:
    print(i.text)