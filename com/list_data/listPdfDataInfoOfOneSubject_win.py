#encoding='utf-8'
from bs4 import BeautifulSoup
import requests
from time import sleep
import http.client

# 网页的请求头
header = {
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
}
http.client._MAXHEADERS = 20000

def is_have_next_page(soup_url):
    response = requests.get(soup_url, headers=header)
    soup = BeautifulSoup(response.text, 'html.parser')
    result_input = soup.find_all('input', {'class': 'btn select'})
    print(result_input[0].get('value'))
    result_p = soup.find_all('p', {'class': 'guide_title'})
    soup_p = BeautifulSoup(str(result_p), 'lxml')
    result_a = soup_p.find_all('a')
    for i in result_a:
        get_page_detail(i.get('href'), result_input[0].get('value'))

#爬取页面想要的数据
def get_page_detail(url,branch_name):
    response = requests.get(url, headers=header,timeout=5000)

    # 通过BeautifulSoup进行解析出每个房源详细列表并进行打印
    soup = BeautifulSoup(response.text, 'html.parser')
    result_pdf = soup.find_all('div', {'class': 'pdf_btn'})[0]
    result_h1 = soup.find_all('h1', {'class': 'text_title'})
    print('url='+url +',branch_name='+result_h1[0].text+',pdf_name='+result_pdf.find('a').get('fn'))
    response.close()



if __name__ == '__main__':
    is_have_next_page('http://guide.medlive.cn/guideline/list?type=guide&year=0&sort=publish&branch=14')




