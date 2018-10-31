from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver import ActionChains

import time

# browser = webdriver.Chrome()
########百度搜索东西
# try:
#     browser.get('https://www.baidu.com')
#     input = browser.find_element_by_id('kw')
#     input.send_keys('python')
#     input.send_keys(Keys.ENTER)
#     wait = WebDriverWait(browser, 10)
#     wait.until(EC.presence_of_all_elements_located((By.ID, 'content_left')))
#     print(browser.current_url)
#     print(browser.get_cookies())
#     print(browser.page_source)
# finally:
# # browser.close()
#     pass

### 访问淘宝
# browser = webdriver.Chrome()
# browser.get('https://www.taobao.com')
### 打印网页代码
# print(browser.page_source)
### 单节点选择
# input_first = browser.find_element_by_id('q')
# input_second = browser.find_element_by_css_selector('#q')    #   #q
# input_third = browser.find_element_by_xpath('//*[@id="q"]')  #    //*[@id="q"]
# print(input_first, input_second, input_third)
####  多节点选择
# lis = browser.find_elements_by_css_selector('.service-bd li')   ##
# print(lis)
#####   节点交互
# input = browser.find_element_by_id('q')
# input.send_keys('iphone')
# time.sleep(3)
# input.clear()
# input.send_keys('iPad')
# button = browser.find_element_by_class_name('btn-search')
# button.click()


##    动作链
# browser = webdriver.Chrome()
# url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
# browser.get(url)
# browser.switch_to.frame('iframeResult')
# source = browser.find_element_by_css_selector('#draggable')
# target = browser.find_element_by_css_selector('#droppable')
# actions = ActionChains(browser)
# actions.drag_and_drop(source, target)
# actions.perform()

#####执行javascript

browser = webdriver.Chrome()
browser.get('https://www.zhihu.com/explore')
browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
browser.execute_script('alert("To Bottom")')