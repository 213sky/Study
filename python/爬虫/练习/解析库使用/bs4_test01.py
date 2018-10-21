### beautiful soup测试
# from bs4 import BeautifulSoup

## 简单测试
# soup = BeautifulSoup('<p>Hello</p>', 'lxml')
# print(soup.p.string)


# html = """
# <html><head><title>The Dormouse's story</title></head>
# <body>
# <p class="title" name="dromouse">342<b>The Dorsdfsdf sto <span>this is span</span></b></p>
# <p class="story"> The Dorsdfsdf sto
# <a herf="http://example.com/elsi" class="sister" id="link1"><!--Elsie--></a>,
# <a herf="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
# <a herf="http://example.com/tillie" class="sister" id="link3">Titlie</a>;
# this s asn s will.</p>
# <p class="story">....</p>
# """
# soup = BeautifulSoup(html, 'lxml')
# print(soup.prettify())     ####  解析的字符串以标准的缩进格式输出
# print("--------------")
# print(soup.title.string)    ##输出指定的节点  中的文本

### 选择元素
# soup = BeautifulSoup(html, 'lxml')
# print(soup.title)
# print(type(soup.title))
# print(soup.title.string)
# print(soup.head)
# print(soup.p) ## 多个p元素就会选择第一个元素进行选择，其他元素忽略


#### 提取信息
# soup = BeautifulSoup(html, 'lxml')
# ##获取名称
# print(soup.title.name)
# ##获取属性
# print(soup.p.attrs)  # 一个 dict对象
# print(soup.p.attrs['name'])
# ##获取内容
# print(soup.p.string)
# ##嵌套选择
# print(soup.head.title)
# print(type(soup.head.title))
# print(soup.head.title.string)
# ###关联选择
#### 子节点和子孙节点
# print(soup.p.contents)  ### 子节点  返回数组
# print(soup.p.children)  ### 子节点  返回iterator
# for i, child in enumerate(soup.p.children):
#     print(i, child)
# print("----------")
# for child in soup.p.children:
#     print(child)
# print("----------")
# print(soup.p.descendants)   ### 子孙节点
# for i, child in enumerate(soup.p.descendants):
#     print(i, child)
# ###父节点和祖先节点
# print(soup.a.parent)  ## 返回父节点整个标签
# print(type(soup.a.parent))
# 所有父节点
# print(soup.prettify())
# print(soup.a.parents)      #######????????????????? 不理解最后输出为什么为4个  2 3相同
# print(list(enumerate(soup.a.parents)))
##### 兄弟节点
# print(soup.a.next_sibling)  # 下一个兄弟节点
# print(soup.a.previous_sibling) # 前一个兄弟节点
# print(list(enumerate(soup.a.next_siblings)))
# print(list(enumerate(soup.a.previous_siblings)))
####提取信息
# print(list(soup.a.parents)[0])
# print(list(soup.a.parents)[0].attrs['class'])



########  方法选择器
# from bs4 import BeautifulSoup
#
# html='''
# <div class="panel">
# <div class="panel-heading">
# <h4>hello</h4>
# </div>
# <div class="panel-body">
# <ul class="list" id="list-1" name="elements">
# <li class="element">Foo</li>
# <li class="element">Bar</li>
# <li class="element">Jay</li>
# </ul>
# <ul class="list list-small" id="list-2">
# <li class="element">Foo</li>
# <li class="element">Bar</li>
# </ul>
# </div>
# </div>
# '''
# soup = BeautifulSoup(html, 'lxml')

#### find_all

#1. name
# print(soup.find_all(name='ul'))
# print(type(soup.find_all(name='ul')[0]))
# for i, ul in enumerate(soup.find_all(name='ul')):
#     print(i, ul.find_all(name='li'))
#     for li in ul.find_all(name='li'):
#         print(li.string)

#2. atrrs
# print(soup.find_all(attrs={"id": "list-1"}))
# print(soup.find_all(attrs={"name": "elements"}))
##  常用属性可以通过
# print(soup.find_all(id="list-1"))
# print(soup.find_all(class_="element"))
###  text 正则表达式
# import re
# print(soup.find_all(text=re.compile("Fo")))


### find
# print(soup.find(name='ul'))  ## find 只会找到第一个就停止了
# print(soup.find(class_='list'))
##  find_parents()  find_paraent()  返回祖先节点，
##  find_next_siblings()  find_next_silbling()     以后的兄弟节点
##  find_previous_sibling()   find_previous_sibling()     前一个兄弟节点
##  find_all_next()   find_next()   返回节点后所有满足条件的节点
##  find_all_previous()  find_previos()  返回节点前所有满足条件的节点


####  CSS 选择器
from bs4 import BeautifulSoup

html='''
<div class="panel .panel-heading">
<div class="panel-heading">
<h4>hello</h4>
</div>
<div class="panel-body">
<ul class="list" id="list-1" name="elements">
<li class="element">Foo</li>
<li class="element">Bar</li>
<li class="element">Jay</li>
</ul>
<ul class="list list-small" id="list-2">
<li class="element">Foo</li>
<li class="element">Bar</li>
</ul>
</div>
</div>
'''
soup = BeautifulSoup(html, 'lxml')
# print('-1--')
# print(soup.select('.panel, .panel-heading'))   ##  选择 .panel  内部的  .panel-heading
# print(len(soup.select('.panel, .panel-heading')))  ## 选择  所有.panel 和 .panel-heading 元素
# print('-1--')
# print(soup.select('ul li'))
# print('-1--')
# print(soup.select('#list-2 .element'))

##嵌套选择
# for ul in soup.select('ul'):
#     print(ul.select('li'))
## 属性获取
# for ul in soup.select('ul'):
#     print(ul['id'])
#     print(ul.attrs['id'])
#     print('--1--')
## 获取文本
for li in soup.select('li'):
    print('Get Text:', li.get_text())
    print('String:', li.string)
    print('--1--')


