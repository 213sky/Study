### beautiful soup测试
from bs4 import BeautifulSoup

## 简单测试
# soup = BeautifulSoup('<p>Hello</p>', 'lxml')
# print(soup.p.string)


html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse">342<b>The Dorsdfsdf sto <span>this is span</span></b></p>
<p class="story"> The Dorsdfsdf sto
<a herf="http://example.com/elsi" class="sister" id="link1"><!--Elsie--></a>,
<a herf="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a herf="http://example.com/tillie" class="sister" id="link3">Titlie</a>;
this s asn s will.</p>
<p class="story">....</p>
"""
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
soup = BeautifulSoup(html, 'lxml')
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
print(list(soup.a.parents)[0])
print(list(soup.a.parents)[0].attrs['class'])


