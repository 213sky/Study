## pyquery  更加适合css选择器
# from pyquery import PyQuery as pq
# html = '''
# <div>
# <ul>
# <li class='item=0'>first item </li>
# <li class='item=1'><a href="link2.html">secod item</a></li>
# <li class='item=0 active'><a href="link3.html"><span class="bold">third item</span></a></li>
# <li class='item=1 active'><a href="link4.html">fourth item</a></li>
# <li class='item=0'><a href="link5.html">fifth item</a></li>
# </ul>
# </div>
# '''
# doc = pq(html)
# print(doc('li'))

## URL 初始化
# doc = pq(url='https://www.baidu.com')
# print(type(doc('title')))
# print(doc('title'))

##  还饿可以从文本读取
# doc = pq(name='***')

######## 基本css选择器
from pyquery import PyQuery as pq
html = '''
<div id="container">
<ul class="list">
<li class="item-0">first item </li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
<li class="item-1 active"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item<ul><li>1</li></ul></a></li>
</ul>
</div>
<div id="container2">
<ul class="list2">
<li class="item-0">first item </li>
<li class="item-12"><a href="link2.html">second  item</a></li>
<li class="item-011 active"><a href="link3.html"><span class="bold">third item</span></a></li>
<li class="item-111 active"><a href="link4.html">fourth item</a></li>
<li class="item-011"><a class="this is test" href="link5.html">fifth item<ul><li>1</li></ul></a></li>
</ul>
</div>
'''
# doc = pq(html)
# print(doc('#container .list li'))
# print(type(doc('#container .list li')))

#### 查找结点
## 子节点
# items = doc('.list')
# print(type(items))
# print(items)
# lis = items.find('li')   ##  查找所有子孙节点的 li
# print(type(lis))
# print(lis)
#
# lis = items.children()  ##  查找子节点的li
# print(type(lis))
# print(lis)

### items = doc('.item-0.active') 查找节点 具有.item-0  并且含有.active属性的节点

## 父节点
# doc = pq(html)
# items = doc('.list')
# items = doc('.item-0')   ###  doc 全部查找
# container = items.parents()
# print(type(container))
# print(container)

###　父节点　们
# items = doc('.item-0.active')
# print(items)
# parents = items.parents()
# print(type(parents))
# print(parents)

###  兄弟节点
# li = doc('.item-0.active')
# print(li.siblings())  ##  查找兄弟节点们
# print('-------')
# print(li.siblings('.active'))   ##  查找兄弟节点们 中间 具有 .active属性的节点
#

### 查出的结果转化成遍历(list)的模式
# li = doc('li').items()
# print(type(li))
# for i, lli in enumerate(li):
#     print(i, lli)

##########  获取信息
# doc = pq(html)
# a = doc('.item-0.active a')
# print(a, type(a))
# print(a.attr('href'))   ##  方法1
# print(a.attr.href)      ##  方法2

# a = doc('a')
# for item in a.items():
#     print(item.attr('href'))

####  获取文本
# doc = pq(html)
# a = doc('.item-0.active a')
# a = doc('a')
# print(a)
# print(a.text())


####  节点操作
# addclass  removeclass
# doc = pq(html)
# li = doc('.item-0.active')
# print(li)
# li.removeClass('active')
# print(li)
# li.addClass('active')
# print(li)

####   attr   text   html
# doc = pq(html)
# li = doc('.item-0.active')
# print(li)
# li.attr('name', 'link')
# print(li)
# li.text('changed item')
# print(li)
# li.html('<span>chaged item</span>')
# print(li)


### remove()
# doc = pq(html)
# wrap = doc('#container')
# print(wrap.text())
# print('-----')
# wrap.find('a').remove()
# print(wrap.text())

### 伪类选择器
doc = pq(html)
li = doc('li:first-child')
print('-----1-----')
print(li)
li = doc('li:last-child')
print('------2----')
print(li)
li = doc('li:nth-child(2)')
print('-----3-----')
print(li)
li = doc('li:gt(2)')   ## :gt 选择器选取 index 值高于指定数的元素
print('-----4-----')
print(li)
li = doc('li:nth-child(2n)')
print('-----5-----')
print(li)
li = doc('li:contains(second)')  ## :contains 选择器选取包含指定字符串的元素。
print('-----6-----')
print(li)



