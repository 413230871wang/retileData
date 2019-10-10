from selenium.webdriver import Chrome
from selenium import webdriver
from time import sleep
import http.client

# 网页的请求头
header = {
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
}
# browser = webdriver.Firefox(executable_path='D:\DownInIE\geckodriver-v0.25.0-win64\geckodriver.exe')
http.client._MAXHEADERS = 20000
#设置后台运行
download_location = '/Users/mfhj-dz-001-068/pythonData/pdfData'
# Firefox headless模式运行
# 设置Firefox下载exe格式的文件，不弹出下载窗，直接下载到指定路径
profile = webdriver.FirefoxProfile()
profile.set_preference('browser.download.dir', download_location)
profile.set_preference('browser.download.folderList', 2)
profile.set_preference('browser.download.manager.showWhenStarting', False)
# 参数 application/octet-stream 表示下载exe文件无需弹窗确认，直接下载
profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'application/octet-stream')

#Firefox headless模式运行
options = webdriver.FirefoxOptions()
options.add_argument('-headless')

#实例化对象时，将设置的Firefox参数传入
driver = webdriver.Firefox(firefox_profile=profile,options=options)
driver.implicitly_wait(30)
# driver.maximize_window()
driver.get('http://www.medlive.cn/auth/login?service=http%3A%2F%2Fguide.medlive.cn%2Fguideline%2Flist%3Ftype%3Dguide%26sort%3Dpublish%26year%3D0%26branch%3D0')
sleep(1)
driver.find_element_by_class_name('login-rightTab').click()
print(driver.find_element_by_id('username').get_attribute('type'))
#输入账号密码
driver.find_element_by_id('username').send_keys("18610229039")
sleep(1)
print('username=' + driver.find_element_by_xpath('//*[@id="username"]').get_attribute('value'))
driver.find_element_by_id('password').send_keys("891655")
sleep(1)
print('password='+driver.find_element_by_id('password').get_attribute('value'))
#单击登录按钮
driver.find_element_by_xpath('//*[@id="loginsubmit"]').click()
sleep(1)
driver.get('http://guide.medlive.cn/guideline/19012')
sleep(1)
print(driver.find_element_by_xpath('//*[@id="_article_viewer_1"]/div/div[2]/a').get_attribute('fn'))
print(driver.find_element_by_xpath('//*[@id="_article_viewer_1"]/div/div[2]/a').is_enabled())
driver.find_element_by_xpath('//*[@id="_article_viewer_1"]/div/div[2]/a').click()
driver.get('http://guide.medlive.cn/guideline/19007')
driver.find_element_by_link_text('下载').click()
