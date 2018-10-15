# 爬虫报测试

# import urllib.request
# import urllib.parse
# import socket
# import urllib.error
# import urllib.request

##基本测试
# response = urllib.request.urlopen("https://www.python.org")
# print(response.read().decode("utf-8"))

##测试提交数据
# data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding="utf8")
# print(data)
# response = urllib.request.urlopen('http://httpbin.org/post', data=data)
# print(response.read())

##测试访问超时
# try:
#     response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)
# except urllib.error.URLError as e:
#     if isinstance(e.reason, socket.timeout):
#         print('time out')

##测试request
# import urllib.request
# request = urllib.request.Request('https://python.org')
# response = urllib.request.urlopen(request)
# print(response.read().decode('utf-8'))
# print(type(request))


##测试request传参
# url = 'http://httpbin.org/post'
# headers = {
#     'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
#     'Host': 'httpbin.org'
# }
# dict = {
#     'name': 'Germey'
# }
# data = bytes(urllib.parse.urlencode(dict), encoding='utf-8')
# req = urllib.request.Request(url=url, data=data, headers=headers, method='POST')
# response = urllib.request.urlopen(req)
# print(response.read().decode('utf-8'))


# 对身份有验证的网页
# from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener
# from urllib.error import URLError
#
# username = 'username'
# password = 'password'
# url = 'http://localhost:5000'
#
# p = HTTPPasswordMgrWithDefaultRealm()
# p.add_password(None, url, username, password)
# auth_handler = HTTPBasicAuthHandler(p)
# opener = build_opener(auth_handler)
#
# try:
#     result = opener.open(url)
#     html = result.read().decode('utf-8')
#     print(html)
# except URLError as e:
#     print(e.reason)


##使用代理ip
# from urllib.error import URLError
# from urllib.request import ProxyHandler, build_opener
#
# proxy_handler = ProxyHandler({
#     'http': 'http://127.0.0.1:9743',
#     'https': 'https://127.0.0.1:9743'
# })
# opener = build_opener(proxy_handler)
# try:
#     response = opener.open('https://www.baiud.com')
#     print(response.read().decode('utf-8'))
# except URLError as e:
#     print(e.reason)


##cookies
##屏幕输出
# cookie = http.cookiejar.CookieJar()
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open('http://www.baidu.com')
# for item in cookie:
#     print(item.name + '=' + item.value)
##文件输出
# filename = 'cookies.txt2'
# # cookie = http.cookiejar.MozillaCookieJar(filename)
# cookie = http.cookiejar.LWPCookieJar(filename)    #保存为lwp文件
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open('http://www.baidu.com')
# cookie.save(ignore_discard=True, ignore_expires=True)
##读取cookie并且访问网站的时候传输过去
# cookie = http.cookiejar.LWPCookieJar()
# cookie.load('cookies.txt2', ignore_discard=True, ignore_expires=True)
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open('http://www.baidu.com')
# print(response.read().decode('utf-8'))


##urlparse
# from urllib.parse import urlparse
#
# result = urlparse('http://www.baidu.com/index.html;user?id=5#comment')
# print(type(result), result)


## requests 能够替换urllib,简单
# import requests
#
# r = requests.get('https://www.baidu.com')
# print(type(r))
# print(r.status_code)
# print(type(r.text))
# print(r.text)
# print(r.cookies)

## requests get
# import requests
# # r = requests.get('http://httpbin.org/get')
# # r = requests.get('http://httpbin.org/get?name=germey&age=22')
# data = {
#     'name':'germey',
#     'age':22
#
# }
# r = requests.get('http://httpbin.org/get', params=data)
# print(r.text)


##抓取知乎测试
# import requests
# import re
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743 Safri/537.36'
# }
# r = requests.get('https://www.zhihu.com/explore', headers=headers)
# pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>', re.S)
# titles = re.findall(pattern, r.text)
# print(titles)

##requests 抓取二进制数据  图片
# import requests
# r = requests.get('https://github.com/favicon.ico')
# # print(r.text)
# # print(r.content)
# with open('favicon.ico', 'wb') as f:
#     f.write(r.content)

##requests 添加heads
# import requests
#
# # r = requests.get("https://www.zhihu.com/explore")
# # print(r.text)
#
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743 Safri/537.36'
# }
# r = requests.get("https://www.zhihu.com/explore", headers=headers)
# print(r.text)


##requests post请求 上传文件
# import requests
# files = {'file':open('favicon.ico', 'rb')}
# r = requests.post('http://httpbin.org/post', files=files)
# print(r.text)


##request cookies
# import requests
# r = requests.get('http://www.baidu.com')
# print(r.cookies)
# for key, value in r.cookies.items():
#     print(key + '=' + value)
#

### requests session
# import requests
##此时与后面对比r.text输出
# requests.get('http://httpbin.org/cookies/set/number/123456789')
# r = requests.get('http://httpbin.org/cookies')
# print(r.text)
##使用同一个会话访问，会保存信息
# s = requests.Session()
# s.get('http://httpbin.org/cookies/set/number/123456789')
# r = s.get('http://httpbin.org/cookies')
# print(r.text)

### requests ssl证书验证  默认get参数verify=True  现在12306不报错暂时无法测试
# import requests
# response = requests.get('http://www.12306.cn')
# print(response.status_code)

###  requests 超时设置
# import requests
# r = requests.get("http://www.taoobao.com", timeout=1)
# print(r.status_code)
###(connect, read, sum总和)
# r = requests.get('http://www.taobao.com', timeout=(5,11,30))

###requests 身份验证
# from requests.auth import HTTPBasicAuth
# r = requests.get('http://localhost:5000', auth=HTTPBasicAuth('username', 'password'))
# print(r.status_code)
## 简化版本
# r = requests.get('http://localhost:5000', auth=('username', 'password'))
# print(r.status_code)


### requests prepared request    结构体化json(类似)
# from requests import Request, Session
#
# url = 'http://httpbin.org/post'
# data = {
#     'name': 'germey'
# }
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743 Safri/537.36'
# }
# s = Session()
# req = Request('POST', url, data=data, headers=headers)
# prepped = s.prepare_request(req)
# r = s.send(prepped)
# print(r.text)
# print(r.headers)


#### 正则表达式  match
# import re
# content = 'Hello 123 4567 World_This is a Regex Demo'
# print(len(content))
# result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}', content)   #当没有匹配的时候，会返回None
# print(result)
# print(result.group())
# print(result.span())

## 正则表达式  search
# import re
# content = 'Hello 123 4567 World_This is a Regex Demo'
# # result = re.search('^Hello\s\d\d\d\s\d{4}\s\w{10}', content)   #当没有匹配的时候，会返回None
# result = re.search('(\d)', content)
# print(result.group())
# if result:
#     print(result.group(1))


### 正则表达式 findall
# import re
# content = 'Hello 123 4567 World_This is a Regex Demo'
# results = re.findall('\d', content)
# print(results)
# print(type(results))
# for result in results:
#     print(result)


### 正则表达式  sub()
# sub()    --->     可以用来替换
# re.sub('\d+', '', content)
#


###  正则表达式   complie()
# import re
# content1 = '2016---'
# pattern = re.compile('\d::')
# result1 = re.sub(pattern, '', content1)





