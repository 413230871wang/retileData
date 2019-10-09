#encoding='utf-8'
import requests
from bs4 import BeautifulSoup
import csv
import codecs
from selenium import webdriver
from time import sleep
import http.client

# 网页的请求头
header = {
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
}
output = codecs.open('D:\pythonFile\\names28.csv','a',encoding='utf-8')
http.client._MAXHEADERS = 20000

def get_page(url):
    # url链接
    response = requests.get(url, headers=header)

    # 通过BeautifulSoup进行解析出每个房源详细列表并进行打印
    soup = BeautifulSoup(response.text, 'html.parser')
    result_div = soup.find_all('div', {'class': 'right_room'})
    soup_p = BeautifulSoup(str(result_div), 'lxml')
    result_p = soup_p.find_all('a')
    for i in result_p:
        is_have_next_page(i.get('href').replace('type=all','type=guide'))

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

def is_have_next_page(soup_url):
    browser = webdriver.Chrome(executable_path='D:\DownInIE\chromedriver_win32\chromedriver.exe')
    browser.maximize_window()

    browser.get(soup_url)
    sleep(1)
    browser.execute_script("""
        (function () {
            var y = 0;
            var step = 210;
            window.scroll(0, 0);
            function f() {
                if (y <= document.body.scrollHeight) {
                    y += step;
                    window.scroll(0, y);
                    setTimeout(f, 100);
                } else {
                    window.scroll(0, 0);
                    document.title += "scroll-done";
                }
            }
            setTimeout(f, 1000);
        })();
        """)
    print("下拉中...")
    while True:
        if "scroll-done" in browser.title:
            break
    else:
        print("还没有拉到最底端...")

    # # url链接
    # url = 'http://guide.medlive.cn/guideline/list?type=guide&year=0&sort=publish&branch=1'
    # response = requests.get(url, headers=header)
    #
    # 通过BeautifulSoup进行解析出每个房源详细列表并进行打印
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    browser.close()
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
    result_h1 = soup.find_all('h1', {'class': 'text_title'})
    result_h3 = soup.find_all('div', {'class': 'one_info clearfix'})
    result_pdf = soup.find_all('div', {'class': 'pdf_info'})[0]
    print('/' + result_pdf.find('a').get('fid') + '/' + result_pdf.find('a').text)
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
        {'科室': branch_name,
         '名称': result_h1[0].text,
         '发布日期': fbrq,
         '英文标题': ywbt,
         '制定者': zdz,
         '出处': cc})
    print('ok')
    response.close()



if __name__ == '__main__':
    # url = 'http://guide.medlive.cn/guideline/list'
    # get_page(url)
    is_have_next_page('http://guide.medlive.cn/guideline/list?type=guide&year=0&sort=publish&branch=28')




