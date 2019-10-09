import requests
import urllib.parse
from bs4 import BeautifulSoup
# 网页的请求头
header = {
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
}
output = open('D:\pythonFile\\names.csv','a',newline='')

url = 'http://guide.medlive.cn/guideline/19002'
response = requests.get(url, headers=header)

# 通过BeautifulSoup进行解析出每个房源详细列表并进行打印
soup = BeautifulSoup(response.text, 'html.parser')
result_h1 = soup.find_all('h1', {'class': 'text_title'})
result_h3 = soup.find_all('div', {'class': 'one_info clearfix'})
result_pdf = soup.find_all('div', {'class': 'pdf_list'})[0]
print('http://webres.medlive.cn/upload/temp/06/4009371/'+result_pdf.find('a').get('fid')+'/'+urllib.parse.quote(result_pdf.find('a').get('fn')).replace('%20','%2B'))
fbrq = ''
ywbt = ''
zdz = ''
cc = ''
for i in result_h3:
    if('发布日期' in i.text):
        fbrq = i.find('p').text
    if ('英文标题' in i.text):
        ywbt = i.find('p').text
    if ('制定者' in i.text):
        zdz = i.find('p').text
    if ('出处' in i.text):
        cc = i.find('p').text
print(fbrq+ywbt+zdz+cc)
# fieldnames = ['科室', '名称', '发布日期', '英文标题', '制定者', '出处']
# writer = csv.DictWriter(output, fieldnames=fieldnames)
# writer.writeheader()
# writer.writerow(soup_p)