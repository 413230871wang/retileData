#encoding='utf-8'
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
import http.client

# 网页的请求头
header = {
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
}
http.client._MAXHEADERS = 20000
#文件下载路径
download_location = 'D:\pythonData\pdfData'
prefs = {'download.default_directory': download_location}
option = webdriver.ChromeOptions()
option.add_experimental_option('prefs',prefs)
#实例化对象时，将设置的Firefox参数传入
browser = webdriver.Chrome(executable_path='D:\DownInIE\chromedriver_win32\chromedriver_win32\chromedriver.exe',options=option)

def is_have_next_page(soup_url):
    # 登陆账号
    browser.get(
        'http://www.medlive.cn/auth/login?service=http%3A%2F%2Fguide.medlive.cn%2Fguideline%2Flist%3Ftype%3Dguide%26sort%3Dpublish%26year%3D0%26branch%3D0')
    sleep(1)
    browser.find_element_by_class_name('login-rightTab').click()
    # 输入账号密码
    browser.find_element_by_id('username').send_keys("18610229039")
    sleep(1)
    browser.find_element_by_id('password').send_keys("891655")
    sleep(1)
    # 单击登录按钮
    browser.find_element_by_id('loginsubmit').click()
    sleep(1)
    # 跳到科室页面刷数据
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
    result_input = soup.find_all('input', {'class': 'btn select'})
    print(result_input[0].get('value'))
    result_p = soup.find_all('p', {'class': 'guide_title'})
    soup_p = BeautifulSoup(str(result_p), 'lxml')
    result_a = soup_p.find_all('a')
    print(len(result_a))
    for i in result_a:
        get_page_detail(i.get('href'))
    browser.close()

#爬取页面想要的数据
def get_page_detail(url):
    try:
        browser.get(url)
        print('url='+url+',pdfName='+browser.find_element_by_link_text('下载').get_attribute('fn'))
    except:
        print(url)



if __name__ == '__main__':
    is_have_next_page('http://guide.medlive.cn/guideline/list?type=guide&year=0&sort=publish&branch=14')




