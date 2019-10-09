import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
import http.client

# 网页的请求头
header = {
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
}
# browser = webdriver.Firefox(executable_path='D:\DownInIE\geckodriver-v0.25.0-win64\geckodriver.exe')
http.client._MAXHEADERS = 20000

def is_have_next_page(soup_url):
    browser = webdriver.Chrome()
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

def get_page_detail(url,branch_name):
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get(url)



if __name__ == '__main__':
    # url = 'http://guide.medlive.cn/guideline/list'
    # get_page(url)
    is_have_next_page('http://guide.medlive.cn/guideline/list?type=guide&year=0&sort=publish&branch=28')