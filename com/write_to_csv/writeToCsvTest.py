import csv
import os
import requests
import codecs
from bs4 import BeautifulSoup

file_dir = 'D:\pythonFile\\names.csv'
# 网页的请求头
header = {
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
}
output = open('D:\pythonFile\\names.csv','a',errors='ignore',encoding='utf-8')
# url链接
url = 'http://guide.medlive.cn/guideline/18918'
response = requests.get(url, headers=header)

# 通过BeautifulSoup进行解析出每个房源详细列表并进行打印
soup = BeautifulSoup(response.text, 'html.parser')
result_h1 = soup.find_all('h1',{'class':'text_title'})
result_h3 = soup.find_all('div',{'class' : 'one_info clearfix'})
soup_p = BeautifulSoup(str(result_h3),'lxml')
result_p = soup_p.find_all('p')
fbrq = ''
ywbt = ''
zdz = ''
cc = ''
for i in result_h3:
    if ('发布日期' in i.text):
        fbrq = i.find('p').text
    if ('英文标题' in i.text):
        ywbt = i.find('p').text
    if ('制定者' in i.text):
        zdz = i.find('p').text
    if ('出处' in i.text):
        cc = i.find('p').text
fieldnames = ['科室', '名称', '发布日期', '英文标题', '制定者', '出处']
writer = csv.DictWriter(output, fieldnames=fieldnames)
# 注意header是个好东西
writer.writerow(
    {'科室': '',
     '名称': result_h1[0].text,
     '发布日期': fbrq,
     '英文标题': ywbt,
     '制定者': zdz,
     '出处': cc})
print('ok')
