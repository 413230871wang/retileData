import csv
import os
import requests
import re
from bs4 import BeautifulSoup

file_dir = 'D:\pythonFile\\names.csv'
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
result_h3 = soup.find_all('div',{'class' : 'one_info clearfix'})
soup_p = BeautifulSoup(str(result_h3),'lxml')
result_p = soup_p.find_all('p')
with open(file_dir, 'a',newline='') as csvfile:
    fieldnames = ['科室','名称','发布日期','英文标题','制定者','出处']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    #注意header是个好东西
    writer.writerow(
        {'科室': '', '名称':result_h1[0].text, '发布日期': result_p[1].text, '英文标题': result_p[2].text, '制定者': result_p[3].text,
         '出处': result_p[4].text})
