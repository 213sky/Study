from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
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

# browser = webdriver.Chrome()
# browser.get('https://www.zhihu.com/explore')
# browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
# browser.execute_script('alert("To Bottom")')


##############  获取节点信息
#####获取属性
# browser = webdriver.Chrome()
# url = 'https://www.zhihu.com/explore'
# browser.get(url)
# logo = browser.find_element_by_id('zh-top-link-logo')
# print(logo)
# print(logo.get_attribute('class'))

### 获取文本值
# browser = webdriver.Chrome()
# url = 'https://www.zhihu.com/explore'
# browser.get(url)
# input = browser.find_element_by_class_name('zu-top-add-question')
# print(input.text)

#### 获取id  位置  标签名和大小
# browser = webdriver.Chrome()
# url = 'https://www.zhihu.com/explore'
# browser.get(url)
# input = browser.find_element_by_class_name('zu-top-add-question')
# print(input.id)
# print(input.location)
# print(input.tag_name)
# print(input.size)


#### 切换 Frame

# browser = webdriver.Chrome()
# url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
# browser.get(url)
# browser.switch_to.frame('iframeResult')
# try:
#     logo = browser.find_element_by_class_name('logo')
# except NoSuchElementException:
#     print('NO LOGO')
# browser.switch_to.parent_frame()
# logo = browser.find_element_by_class_name('logo')
# print(logo)
# print(logo.text)


##############  延时等待 !!!!!!!!!!!!!!!!!!!

# ###隐士等待
# browser = webdriver.Chrome()
# browser.implicitly_wait(10)            ### dom找不到指定元素，就会立即抛出错误，当时设置此参数，就会等待一定时间后抛出错误
# browser.get('https://www.zhihu.com/explore')
# input = browser.find_element_by_class_name('zu-top-add-question1')  #### 正确zu-top-add-question
# print(input)

### 显示等待

# browser = webdriver.Chrome()
# browser.get('https://www.taobao.com')
# wait = WebDriverWait(browser, 10)
# input = wait.until(EC.presence_of_all_elements_located((By.ID, 'q')))
# button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-search1')))


############# 前进和后退

# browser = webdriver.Chrome()
# browser.get('https://www.baidu.com')
# browser.get('https://www.taobao.com')
# browser.get('https://www.python.org')
# browser.back()
# time.sleep(1)
# browser.forward()
# browser.close()

###### cookies
# browser = webdriver.Chrome()
# browser.get('https://www.zhihu.com/explore')
# print(browser.get_cookies())
# browser.add_cookie({'name': 'name', 'domain': 'www.zhihu.com', 'value': 'germey'})
# print(browser.get_cookies())
# browser.delete_all_cookies()
# print(browser.get_cookies())



###### 选项卡管理

# browser = webdriver.Chrome()
# browser.get('http://www.baidu.com')
# browser.execute_script('window.open()')
# print(browser.window_handles)
# # browser.switch_to_window(browser.window_handles[1])   ### switch_to_window此方法已经停用了
# browser.switch_to.window(browser.window_handles[1])
# browser.get('https://www.taobao.com')
# time.sleep(1)
# # browser.switch_to_window(browser.window_handles[0])
# browser.switch_to.window(browser.window_handles[0])
# browser.get('https://python.org')



######## 异常处理

# browser = webdriver.Chrome()
# browser.get('https://www.baidu.com')
# browser.find_element_by_id('hello')


browser = webdriver.Chrome()
try:
    browser.get('https://www.baidu.com')
except TimeoutException:
    print('Time Out')

try:
    browser.find_element_by_id('hello')
except NoSuchElementException:
    print('No Element')
finally:
    browser.close()