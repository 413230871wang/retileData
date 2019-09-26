import requests
import re
from bs4 import BeautifulSoup

# 网页的请求头
header = {
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
}

output = open('D:\pythonFile\medsci.txt','a',encoding='utf-8')
# url链接
url = 'http://www.medsci.cn/guideline/show_article.do?id=6b2e81c001398a82'
response = requests.get(url, headers=header)
print(response)
soup = BeautifulSoup(response.text, 'html.parser')
print(soup)
result_h3 = soup.find_all('div',{'class' :'breadcrumb container'})
print(result_h3)
if(len(result_h3) ==0):
    print("OMG")
soup_p = BeautifulSoup(str(result_h3),'lxml')
result_p = soup_p.find_all('a')[len(soup_p)+1].text
print(result_p)
# 通过BeautifulSoup进行解析出每个房源详细列表并进行打印
soup = BeautifulSoup(response.text, 'html.parser')
result_h3 = soup.find_all('div',{'class' : 'one_info clearfix'})
# soup_p = BeautifulSoup(str(result_h3),'lxml')
for i in result_h3:
    result_p = i.text
    print(result_p)

output.close();
