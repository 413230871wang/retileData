import requests
import re
from bs4 import BeautifulSoup

# 网页的请求头
header = {
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
}

# url链接
url = 'http://guide.medlive.cn/guideline/list?type=all&year=0&sort=publish&branch=1'
response = requests.get(url, headers=header)

# 通过BeautifulSoup进行解析出每个房源详细列表并进行打印
soup = BeautifulSoup(response.text, 'html.parser')
result_input = soup.find_all('input',{'class':'btn select'})
print(result_input[0].get('value'))
result_p = soup.find_all('p',{'class':'guide_title'})
soup_p = BeautifulSoup(str(result_p),'lxml')
result_a = soup_p.find_all('a')
for i in result_a:
    print(i.get('href'))