import requests
from bs4 import BeautifulSoup
import re
import csv

# 网页的请求头
header = {
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
}
output = open('D:\pythonFile\\names.csv','a',newline='')

def get_page(url):
    # url链接
    response = requests.get(url, headers=header)

    # 通过BeautifulSoup进行解析出每个房源详细列表并进行打印
    soup = BeautifulSoup(response.text, 'html.parser')
    result_div = soup.find_all('div', {'class': 'right_room clearfix'})
    soup_p = BeautifulSoup(str(result_div), 'lxml')
    result_p = soup_p.find_all('a')
    for i in result_p:
        get_next_level(i.get('href'))

    output.close()

def get_next_level(url):
    response = requests.get(url, headers=header)

    # 通过BeautifulSoup进行解析出每个房源详细列表并进行打印
    soup = BeautifulSoup(response.text, 'html.parser')
    result_input = soup.find_all('input', {'class': 'btn select'})
    result_p = soup.find_all('p', {'class': 'guide_title'})
    soup_p = BeautifulSoup(str(result_p), 'lxml')
    result_a = soup_p.find_all('a')
    for i in result_a:
        get_page_detail(i.get('href'),result_input[0].get('value'))

# def is_have_next_page(soup_idex):
#     result_next_page = soup_idex.find_all('a',text='下一页')
#     if len(result_next_page) != 0:
#         x_str = [x.get("href") for x in result_next_page][0]
#         next_url = pre_url_next_level + x_str
#         get_next_level(next_url,pre_url_next_level)
#     else:
#         print('没有下一页')

#爬取页面想要的数据
def get_page_detail(url,branch_name):
    response = requests.get(url, headers=header)

    # 通过BeautifulSoup进行解析出每个房源详细列表并进行打印
    soup = BeautifulSoup(response.text, 'html.parser')
    result_h1 = soup.find_all('h1', {'class': 'text_title'})
    result_h3 = soup.find_all('div', {'class': 'one_info clearfix'})
    soup_p = BeautifulSoup(str(result_h3), 'lxml')
    result_p = soup_p.find_all('p')
    fieldnames = ['科室', '名称', '发布日期', '英文标题', '制定者', '出处']
    writer = csv.DictWriter(output, fieldnames=fieldnames)
    # 注意header是个好东西
    writer.writerow(
        {'科室': branch_name, '名称': result_h1[0].text, '发布日期': result_p[1].text, '英文标题': result_p[2].text,
         '制定者': result_p[3].text,
         '出处': result_p[4].text})



if __name__ == '__main__':
    url = 'http://guide.medlive.cn/guideline/list'
    get_page(url)




