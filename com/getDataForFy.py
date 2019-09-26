import requests
from bs4 import BeautifulSoup
import re

# 网页的请求头
header = {
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
}
url = 'http://www.medsci.cn/guideline/'
pre_url = 'http://www.medsci.cn'
pre_url_next_level = 'http://www.medsci.cn/guideline/'
output = open('D:\pythonFile\medsci.txt','a',encoding='utf-8')
def get_page(url,preUrl):
    # url链接

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
        #把每一个url输出(输出每一个科室)
        for j in result_href:
            href_str = pre_url+j.get('href')
            print(href_str)
            get_next_level(href_str,pre_url_next_level)

    output.close()

def get_next_level(url,pre_url):
    response = requests.get(url, headers=header)

    # 通过BeautifulSoup进行解析出每个房源详细列表并进行打印
    soup_idex = BeautifulSoup(response.text, 'html.parser')
    result_li = soup_idex.find_all('div', {'class': 'news3'})

    is_have_next_page(soup_idex)

    for i in result_li:
        page_url = str(i)
        soup = BeautifulSoup(page_url, 'html.parser')
        # 由于通过class解析的为一个列表，所以只需要第一个参数
        result_href = soup.find_all('a')
        x_str = [x.get("href") for x in result_href][0]
        # 把每一个url输出(输出每一个科室)
        href_str = pre_url + x_str
        get_page_detail(href_str)

def is_have_next_page(soup_idex):
    result_next_page = soup_idex.find_all('a',text='下一页')
    if len(result_next_page) != 0:
        x_str = [x.get("href") for x in result_next_page][0]
        next_url = pre_url_next_level + x_str
        get_next_level(next_url,pre_url_next_level)
    else:
        print('没有下一页')

#爬取页面想要的数据
def get_page_detail(url):
    response = requests.get(url, headers=header)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        result_h3 = soup.find_all('div', {'class': 'breadcrumb container'})
        if (len(result_h3) == 0):
            return
        soup_p = BeautifulSoup(str(result_h3), 'lxml')
        result_p = soup_p.find_all('a')[len(soup_p)+1].text
        print(result_p)
        output.write(result_p + '\n')
        # 通过BeautifulSoup进行解析出每个房源详细列表并进行打印
        soup = BeautifulSoup(response.text, 'html.parser')
        result_h3 = soup.find_all('h3')
        soup_p = BeautifulSoup(str(result_h3), 'lxml')
        result_p = soup_p.find_all('p')
        for i in result_p:
            if (re.match('指南名称', i.text) or re.match('发布机构', i.text) or re.match('发布日期', i.text)):
                print(i.text)  # 这里取标签text
                output.write(i.text + '\n')



if __name__ == '__main__':
    get_page(url,pre_url)




