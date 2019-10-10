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
chrome_options = webdriver.ChromeOptions()
chrome_options.headless = True
chrome_options.add_argument('--disable-gpu')

prefs = {'download.prompt_for_download': False, 'download.directory_upgrade': True, 'safebrowsing.enabled': False, 'safebrowsing.disable_download_protection': True}

chrome_options.add_experimental_option('prefs', prefs)
driver = Chrome(options=chrome_options)

driver.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')

params = {'cmd': 'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': download_location}}
command_result = driver.execute("send_command", params)
print("response from browser:"+str(command_result))
for key in command_result:
    print("result:" + key + ":" + str(command_result[key]))
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
sleep(10)
driver.close()
