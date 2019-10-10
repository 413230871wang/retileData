#!/usr/bin/python
# _*_ coding:utf-8 _*_
# Author:xiaoshubiao
# Time : 2018/8/14 14:57
import time
from selenium.webdriver import Chrome
from selenium import webdriver
download_location = '/Users/mfhj-dz-001-068/pythonData/pdfData'
chrome_options = webdriver.ChromeOptions()
prefs = {'download.default_directory': download_location,
         'download.prompt_for_download': False,
         'download.directory_upgrade': True,
         'safebrowsing.enabled': False,
         'safebrowsing.disable_download_protection': True}

chrome_options.add_experimental_option('prefs', prefs)
chrome_options.add_argument("--headless")
driver = Chrome(chrome_options=chrome_options)
driver.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')

params = {'cmd': 'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': download_location}}
command_result = driver.execute("send_command", params)
print("response from browser:")
for key in command_result:
    print("result:" + key + ":" + str(command_result[key]))

# 这里是随便选了一个可以下载的连接，无心骚扰。
driver.get("http://www.yundama.com/apidoc/YDM_SDK.html")
clone_box = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/p[11]/a')
clone_box.click()
time.sleep(10)
driver.quit()