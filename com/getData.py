import requests
from bs4 import BeautifulSoup
import re

# 网页的请求头
header = {
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
}
# url链接
url = 'http://www.medsci.cn/guideline/'
pre_url = 'http://www.medsci.cn'
response = requests.get(url, headers=header)

# 通过BeautifulSoup进行解析出每个房源详细列表并进行打印
soup = BeautifulSoup(response.text, 'html.parser')
result_li = soup.find_all('div', {'class': 'nk_list'})
for i in result_li:
    # 由于BeautifulSoup传入的必须为字符串，所以进行转换
    page_url = str(i)
    soup = BeautifulSoup(page_url, 'html.parser')
    # 由于通过class解析的为一个列表，所以只需要第一个参数
    result_href = soup.find_all('a')
    #把每一个url输出
    for j in result_href:
        href_str = pre_url+j.get('href')
        print(href_str)

