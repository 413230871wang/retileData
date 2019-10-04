import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep

# 网页的请求头
header = {
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
}
# browser = webdriver.Firefox(executable_path='D:\DownInIE\geckodriver-v0.25.0-win64\geckodriver.exe')
browser = webdriver.Chrome(executable_path='D:\DownInIE\chromedriver_win32\chromedriver.exe')
browser.maximize_window()

browser.get('http://guide.medlive.cn/guideline/list?type=guide&year=0&sort=publish&branch=5')
sleep(3)
# for i in range(1,6):
#     print(1)
#     browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
#     sleep(1)
browser.execute_script("""
    (function () {
        var y = 0;
        var step = 110;
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
# time.sleep(180)
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
result_input = soup.find_all('input',{'class':'btn select'})
print(result_input[0].get('value'))
result_p = soup.find_all('p',{'class':'guide_title'})
soup_p = BeautifulSoup(str(result_p),'lxml')
result_a = soup_p.find_all('a')
for i in result_a:
    print(i.get('href'))