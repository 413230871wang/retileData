#encoding='utf-8'
from selenium import webdriver
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
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
browser = webdriver.Chrome(executable_path='D:\DownInIE\chromedriver_win32\chromedriver_win32_79\chromedriver.exe',options=option)

def is_have_next_page(strs):
    browser.maximize_window()
    # 登陆账号
    browser.get(
        'https://www.incopat.com/newLogin?locale=zh')
    sleep(1)
    # 输入账号密码
    browser.find_element_by_id('u').send_keys("yxxxfxpj")
    sleep(1)
    browser.find_element_by_id('p').send_keys("yxxxfxpj123")
    sleep(1)
    # 单击登录按钮
    browser.find_element_by_id('loginBtn').click()
    # 如果有弹出框 点击确定
    sleep(2)
    browser.switch_to.alert.accept()
    # 开始查询数据
    browser.find_element_by_id('searchValue').send_keys('(IN=(赵维莅)) AND (AP=(上海交通大学) OR AP=(上海交通大学医学院附属瑞金医院;上海血液学研究所医学基因组学国家重点实验室))')
    sleep(1)
    browser.find_element_by_class_name('btn').click()
    sleep(1)
    browser.find_element_by_class_name('first_li3').click()
    browser.find_element_by_id('anMerge').click()
    result = EC.alert_is_present()(browser)
    if result:
        result.accept()
    sleep(3)
    browser.find_element_by_xpath('//*[@id="rightTool"]/ul/li[1]').click()
    sleep(2)
    browser.find_element_by_xpath('//*[@id="downloadResultDiv"]/div/div[2]/div[1]/ul/li[4]/a[2]').click()
    sleep(2)
    browser.find_element_by_xpath('//*[@id="downloadResultDiv"]/div/div[2]/div[2]/input[2]').click()
    sleep(2)
    for str in strs:
        try:
            browser.find_element_by_id('queryShow').clear()
            browser.find_element_by_id('queryShow').send_keys(str)
            sleep(3)
            browser.find_element_by_id('solrSearchUpdate').click()
            sleep(3)
            browser.find_element_by_class_name('first_li3').click()
            browser.find_element_by_id('anMerge').click()
            result = EC.alert_is_present()(browser)
            if result:
                result.accept()
            sleep(3)
            browser.find_element_by_xpath('//*[@id="rightTool"]/ul/li[1]').click()
            sleep(1)
            browser.find_element_by_xpath('//*[@id="downloadResultDiv"]/div/div[2]/div[1]/ul/li[4]/a[2]').click()
            sleep(1)
            browser.find_element_by_xpath('//*[@id="downloadResultDiv"]/div/div[2]/div[2]/input[2]').click()
            if result:
                result.accept()
                sleep(1)
                browser.find_element_by_id('closeSaveResultLayer').click()
                sleep(1)
            sleep(2)
        except:
            print(str+'有问题')
#爬取页面想要的数据
def get_page_detail(url):
    try:
        browser.get(url)
        browser.find_element_by_link_text('下载').click()
    except:
        print(url)


if __name__ == '__main__':
    people = [
'(IN=(杨清武)) AND (AP=(中国人民解放军第三军医大学) OR AP=(陆军军医大学新桥医院))',
'(IN=(张浩)) AND (AP=(中国医学科学院阜外医院) OR AP=(中国医学科学院阜外医院))',
'(IN=(赵晨)) AND (AP=(南京医科大学) OR AP=(南京医科大学第一附属医院))',
'(IN=(白晓春)) AND (AP=(南方医科大学) OR AP=(南方医科大学第三附属医院))',
'(IN=(卜军)) AND (AP=(上海交通大学) OR AP=(上海交通大学医学院附属仁济医院))',
'(IN=(范志朋)) AND (AP=(首都医科大学) OR AP=(首都医科大学附属北京口腔医院))',
'(IN=(韩鸿宾)) AND (AP=() OR AP=(北京大学第三医院))',
'(IN=(贾立军)) AND (AP=(复旦大学) OR AP=(复旦大学附属肿瘤医院))',
'(IN=(李春英)) AND (AP=(中国人民解放军第四军医大学) OR AP=(第四军医大学西京医院))',
'(IN=(石明)) AND (AP=(中山大学) OR AP=(中山大学肿瘤防治中心))',
'(IN=(王辉)) AND (AP=(北京大学) OR AP=(北京大学人民医院))',
'(IN=(王平)) AND (AP=(同济大学) OR AP=(上海市第十人民医院))',
'(IN=(王延江)) AND (AP=(中国人民解放军第三军医大学) OR AP=(第三军医大学附属大坪医院))',
'(IN=(徐明)) AND (AP=(北京大学) OR AP=(北京大学第三医院))',
'(IN=(徐骁)) AND (AP=(浙江大学) OR AP=(浙江大学医学院附属第一医院))',
'(IN=(杨莉)) AND (AP=(北京大学) OR AP=(北京大学第一医院))',
'(IN=(虞先濬)) AND (AP=(复旦大学) OR AP=(复旦大学附属肿瘤医院复旦大学胰腺肿瘤研究所))',
'(IN=(陈莉莉)) AND (AP=(华中科技大学) OR AP=(华中科技大学同济医学院附属协和医院))',
'(IN=(段胜仲)) AND (AP=(上海交通大学) OR AP=(上海交通大学医学院附属第九人民医院))',
'(IN=(李华斌)) AND (AP=(复旦大学) OR AP=(复旦大学附属眼耳鼻喉科医院))',
'(IN=(罗俊航)) AND (AP=(中山大学) OR AP=(中山大学附属第一医院))',
'(IN=(商洪才)) AND (AP=(北京中医药大学) OR AP=(北京中医药大学东直门医院))',
'(IN=(孙爱军)) AND (AP=(复旦大学) OR AP=(复旦大学附属中山医院))',
'(IN=(田梅)) AND (AP=(浙江大学) OR AP=(浙江大学医学院附属第二医院))',
'(IN=(王菲)) AND (AP=(中国医科大学) OR AP=(中国医科大学附属第一医院))',
'(IN=(吴晨)) AND (AP=(中国医学科学院肿瘤医院) OR AP=(中国医学科学院肿瘤医院))',
'(IN=(徐辉雄)) AND (AP=(同济大学) OR AP=(同济大学附属第十人民医院))',
'(IN=(赵曜)) AND (AP=(复旦大学) OR AP=(复旦大学附属华山医院))',
'(IN=(黄晓军)) AND (AP=(北京大学) OR AP=(北京大学人民医院))',
'(IN=(陈吉华)) AND (AP=(第四军医大学) OR AP=(第四军医大学口腔医学院))',
'(IN=(韩英)) AND (AP=(第四军医大学) OR AP=(第四军医大学西京医院))',
'(IN=(张国君)) AND (AP=(汕头大学) OR AP=(汕头大学医学院附属肿瘤医院))',
'(IN=(范先群)) AND (AP=(上海交通大学) OR AP=(上海交通大学医学院附属第九人民医院))',
'(IN=(刘颖斌)) AND (AP=(上海交通大学) OR AP=(上海交通大学医学院附属新华医院))',
'(IN=(曾凡一)) AND (AP=(上海交通大学) OR AP=(上海市儿童医院))',
'(IN=(张罗)) AND (AP=(首都医科大学) OR AP=(首都医科大学附属北京同仁医院))',
'(IN=(梁廷波)) AND (AP=(浙江大学) OR AP=(浙江大学医学院附属第二医院))',
'(IN=(翁建平)) AND (AP=(中山大学) OR AP=(中山大学附属第三医院))',
'(IN=(余学清)) AND (AP=(中山大学) OR AP=(中山大学附属第一医院))',
'(IN=(周俭)) AND (AP=(复旦大学) OR AP=(复旦大学附属中山医院))',
'(IN=(钦伦秀)) AND (AP=(复旦大学) OR AP=(复旦大学附属中山医院))',
'(IN=(刘连新)) AND (AP=(哈尔滨医科大学) OR AP=(哈尔滨医科大学附属第一医院))',
'(IN=(程树群)) AND (AP=(第二军医大学) OR AP=(第二军医大学东方肝胆外科医院))',
'(IN=(孙倍成)) AND (AP=(南京大学) OR AP=(南京医科大学第一附属医院))',
'(IN=(李维勤)) AND (AP=(南京大学) OR AP=(南京军区南京总医院))',
'(IN=(蒋欣泉)) AND (AP=(上海交通大学) OR AP=(上海交通大学医学院附属第九人民医院))',
'(IN=(杨胜勇)) AND (AP=(四川大学) OR AP=(四川大学华西医院))',
'(IN=(王振宁)) AND (AP=(中国医科大学) OR AP=(中国医科大学附属第一医院))',
'(IN=(毛颖)) AND (AP=(复旦大学) OR AP=(复旦大学附属华山医院))',
'(IN=(黄恺)) AND (AP=(华中科技大学) OR AP=(华中科技大学同济医学院附属协和医院))',
'(IN=(曾春雨)) AND (AP=(第三军医大学) OR AP=(第三军医大学大坪医院))',
'(IN=(彭军)) AND (AP=(山东大学) OR AP=(山东大学齐鲁医院))',
'(IN=(林厚文)) AND (AP=(上海交通大学) OR AP=(上海交通大学医学院附属仁济医院))',
'(IN=(孙晓东)) AND (AP=(上海交通大学) OR AP=(上海市第一人民医院))',
'(IN=(戈宝学)) AND (AP=(同济大学) OR AP=(上海市肺科医院))',
'(IN=(吉训明)) AND (AP=(首都医科大学) OR AP=(首都医科大学宣武医院))',
'(IN=(龚启勇)) AND (AP=(四川大学) OR AP=(四川大学华西医院))',
'(IN=(黄灿华)) AND (AP=(四川大学) OR AP=(四川大学华西医院))',
'(IN=(冯世庆)) AND (AP=(天津医科大学) OR AP=(天津医科大学总医院))',
'(IN=(田梅)) AND (AP=(浙江大学) OR AP=(浙江大学医学院附属第二医院))',
'(IN=(徐骁)) AND (AP=(浙江大学) OR AP=(浙江大学医学院附属第一医院))',
'(IN=(张烜)) AND (AP=(北京协和医学院) OR AP=(中国医学科学院北京协和医院))',
'(IN=(荆志成)) AND (AP=(北京协和医学院) OR AP=(中国医学科学院阜外心血管病医院))',
'(IN=(曹彬)) AND (AP=(首都医科大学) OR AP=(中日友好医院))',
'(IN=(区景松)) AND (AP=(中山大学) OR AP=(中山大学附属第一医院))',
'(IN=(康铁邦)) AND (AP=(中山大学) OR AP=(中山大学肿瘤防治中心))',
'(IN=(曾木圣)) AND (AP=(中山大学) OR AP=(中山大学肿瘤防治中心))',
'(IN=(邓旭亮)) AND (AP=(北京大学口腔医院) OR AP=(北京大学口腔医院))',
'(IN=(赵曜)) AND (AP=(复旦大学附属华山医院) OR AP=(复旦大学附属华山医院))',
'(IN=(徐彦辉)) AND (AP=(复旦大学) OR AP=(复旦大学附属肿瘤医院))',
'(IN=(王琳)) AND (AP=(华中科技大学) OR AP=(华中科技大学同济医学院附属协和医院))',
'(IN=(屈延)) AND (AP=(第四军医大学唐都医院) OR AP=(第四军医大学唐都医院))',
'(IN=(李春英)) AND (AP=(第四军医大学西京医院) OR AP=(第四军医大学西京医院))',
'(IN=(刘祖国)) AND (AP=(厦门大学) OR AP=(厦门大学附属厦门眼科中心))',
'(IN=(张澄)) AND (AP=(山东大学齐鲁医院) OR AP=(山东大学齐鲁医院))',
'(IN=(赵维莅)) AND (AP=(上海交通大学附属瑞金医院) OR AP=(上海交通大学附属瑞金医院))',
'(IN=(丁楅森)) AND (AP=(四川大学华西第二医院) OR AP=(四川大学华西第二医院))',
'(IN=(李红良)) AND (AP=(武汉大学人民医院) OR AP=(武汉大学人民医院))',
'(IN=(郑哲)) AND (AP=(中国医学科学院阜外医院) OR AP=(中国医学科学院阜外医院))',
'(IN=(陈旻)) AND (AP=(北京大学) OR AP=(北京大学第一医院))',
'(IN=(李悦)) AND (AP=(哈尔滨医科大学) OR AP=(哈尔滨医科大学附属第一医院))',
'(IN=(罗招庆)) AND (AP=(吉林大学) OR AP=(吉林大学白求恩第一医院))',
'(IN=(陈发明)) AND (AP=(第四军医大学) OR AP=(第四军医大学口腔医院))',
'(IN=(陶凌)) AND (AP=(第四军医大学) OR AP=(第四军医大学西京医院))',
'(IN=(杨清武)) AND (AP=(第三军医大学) OR AP=(第三军医大学新桥医院))',
'(IN=(卜军)) AND (AP=(上海交通大学) OR AP=(上海交通大学医学院附属仁济医院))',
'(IN=(毕宇芳)) AND (AP=(上海交通大学) OR AP=(上海交通大学瑞金医院))',
'(IN=(吴安华)) AND (AP=(中国医科大学) OR AP=(中国医科大学附属第一医院))',
'(IN=(雷光华)) AND (AP=(中南大学) OR AP=(中南大学湘雅医院))',
'(IN=(周永胜)) AND (AP=(北京大学) OR AP=(北京大学口腔医院))',
'(IN=(夏云龙)) AND (AP=(大连医科大学) OR AP=(大连医科大学附属第一医院))',
'(IN=(赵晨)) AND (AP=(复旦大学) OR AP=(南京医科大学第一附属医院))',
'(IN=(汪辉)) AND (AP=(华中科技大学) OR AP=(华中科技大学同济医学院附属同济医院))',
'(IN=(程翔)) AND (AP=(华中科技大学) OR AP=(华中科技大学同济医学院附属协和医院))',
'(IN=(董海龙)) AND (AP=(空军军医大学（第四军医大学）) OR AP=(空军军医大学西京医院))',
'(IN=(王延江)) AND (AP=(陆军军医大学（第三军医大学）) OR AP=(陆军军医大学大坪医院))',
'(IN=(张曦)) AND (AP=(陆军军医大学（第三军医大学）) OR AP=(陆军军医大学新桥医院))',
'(IN=(段胜仲)) AND (AP=(上海交通大学) OR AP=(上海交通大学医学院附属第九人民医院))',
'(IN=(贾立军)) AND (AP=(上海中医药大学) OR AP=(上海中医药大学龙华医院))',
'(IN=(李涛)) AND (AP=(四川大学) OR AP=(四川大学华西医院))',
'(IN=(陆林)) AND (AP=(北京大学) OR AP=(北京大学第六医院))',
'(IN=(乔杰)) AND (AP=(北京大学) OR AP=(北京大学第三医院))',
'(IN=(董家鸿)) AND (AP=(清华大学) OR AP=(北京清华长庚医院))',
'(IN=(詹启敏)) AND (AP=(北京协和医学院) OR AP=(北京肿瘤医院))',
'(IN=(樊嘉)) AND (AP=(复旦大学附属中山医院) OR AP=(复旦大学附属中山医院))',
'(IN=(葛均波)) AND (AP=(复旦大学) OR AP=(复旦大学附属中山医院))',
'(IN=(夏照帆（女）)) AND (AP=(第二军医大学) OR AP=(海军军医大学附属长海医院))',
'(IN=(李兆申)) AND (AP=(海军军医大学) OR AP=(海军军医大学附属长海医院))',
'(IN=(孙颖浩)) AND (AP=(第二军医大学) OR AP=(海军军医大学附属长海医院))',
'(IN=(张英泽)) AND (AP=(河北医科大学) OR AP=(河北医科大学第三医院))',
'(IN=(陈孝平 )) AND (AP=(华中科技大学 ) OR AP=(华中科技大学同济医学院附属同济医院))',
'(IN=(马丁)) AND (AP=(华中科技大学) OR AP=(华中科技大学同济医学院附属同济医院))',
'(IN=(卞修武)) AND (AP=(陆军军医大学) OR AP=(陆军军医大学西南医院))',
'(IN=(王学浩)) AND (AP=(南京医科大学) OR AP=(南京医科大学第一附属医院))',
'(IN=(于金明)) AND (AP=(--) OR AP=(山东省肿瘤医院))',
'(IN=(张志愿)) AND (AP=(上海交通大学) OR AP=(上海交通大学医学院附属第九人民医院))',
'(IN=(宁光)) AND (AP=(上海交通大学) OR AP=(上海交通大学医学院附属瑞金医院))',
'(IN=(陈义汉 )) AND (AP=(同济大学) OR AP=(上海市东方医院))',
'(IN=(韩雅玲（女）)) AND (AP=(沈阳军区总医院) OR AP=(沈阳军区总医院))',
'(IN=(赵继宗)) AND (AP=(首都医科大学) OR AP=(首都医科大学附属北京天坛医院))',
'(IN=(韩德民)) AND (AP=(首都医科大学) OR AP=(首都医科大学附属北京同仁医院))',
'(IN=(黄荷凤（女）)) AND (AP=(上海交通大学) OR AP=(中国福利会国际和平妇幼保健院))',
'(IN=(王福生 )) AND (AP=(#) OR AP=(中国人民解放军第三〇二医院))',
'(IN=(高长青)) AND (AP=(解放军总医院) OR AP=(中国人民解放军总医院))',
'(IN=(顾瑛（女） )) AND (AP=(#) OR AP=(中国人民解放军总医院))',
'(IN=(赵玉沛)) AND (AP=(北京协和医学院) OR AP=(中国医学科学院北京协和医院))',
'(IN=(郎景和)) AND (AP=(北京协和医学院) OR AP=(中国医学科学院北京协和医院))',
'(IN=(胡盛寿)) AND (AP=(北京协和医学院) OR AP=(中国医学科学院阜外医院))',
'(IN=(顾东风)) AND (AP=(中国医学科学院阜外医院) OR AP=(中国医学科学院阜外医院))',
'(IN=(林东昕)) AND (AP=(北京协和医学院) OR AP=(中国医学科学院肿瘤医院))',
'(IN=(赫捷)) AND (AP=(北京协和医学院) OR AP=(中国医学科学院肿瘤医院))',
'(IN=(王辰)) AND (AP=(中日友好医院) OR AP=(中日友好医院))'
]
    is_have_next_page(people)




