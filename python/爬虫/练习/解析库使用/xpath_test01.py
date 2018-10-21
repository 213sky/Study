
### 自动修复 最后一个缺漏的li闭合标签
# from lxml import etree
# text = '''
# <div class="nav">
#             <ul class="navbar">
#                 <li><a href="/" data-act="home-click">首页</a></li>
#                 <li><a href="/films" data-act="movies-click">电影</a></li>
#                 <li><a href="/cinemas" data-act="cinemas-click">影院</a></li>
#
#                 <li><a href="/board" data-act="board-click" class="active">榜单</a></li>
#                 <li><a href="/news" data-act="hotNews-click">热点</a>
#             </ul>
#         </div>
# '''
# html = etree.HTML(text)
# result = etree.tostring(html)
# print(result.decode('utf-8'))


### 自动修复
# from lxml import etree
# html = etree.parse('test.html', etree.HTMLParser())
# result = etree.tostring(html)
# print(result.decode('utf-8'))

# 选取模式
### //(从当前节点选区子孙节点)模式选取节点  //*   ,  选取指定节点  //li
### /(从当前节点选区子节点)
### @(选取属性)
### ..(选取当前节点的父节点)
# from lxml import etree
# html = etree.parse('test.html', etree.HTMLParser())
###########所有节点
# result = html.xpath('//*')
# result = html.xpath('//li')
###########子节点
# result = html.xpath('//li/a')
# result = html.xpath('//ul/a')
###########父节点
# result = html.xpath('//a[@href="link4.html"]/../@class')
# result = html.xpath('//a[@href="link4.html"]/parent::* /@class')
###########属性匹配
# result = html.xpath('//li[@class="item-0"]')
###########文本获取
# result = html.xpath('//li[@class="item-0"]/text()')  #无法获取
# result = html.xpath('//li[@class="item-0"]/a/text()')
# result = html.xpath('//li[@class="item-0"]//text()')   ## 会获取杂项
###########属性获取
# result = html.xpath('//li//a/@href')   ## 会获取杂项
# print(result)


###属性多值匹配   多属性匹配
# from lxml import etree
# text = '''
# <li class="li li-first" name="item"><a href="link.html">first item</a></li>
# '''
# html = etree.HTML(text)
###属性多值匹配
# result = html.xpath('//li[@class="li"]/a/text()')   ## li属性具有多值，只用这么一个单属性无法获取
# result = html.xpath('//li[contains(@class, "li")]/a/text()')
###  多属性匹配
# result = html.xpath('//li[contains(@class, "li") and @name="item"]/a/text()')
# print(result)


### 按序选择
# from lxml import etree
# text = '''
# <div>
#     <ul>
#         <li class="item-0"><a href="link1.html">首页01</a></li>
#         <li class="item-1"><a href="link2.html">电影02</a></li>
#         <li class="item-inactive"><a href="link3.html">影院03</a></li>
#         <li class="item-0"><a href="link4.html">榜单04</a></li>
#         <li class="item-1"><a href="link5.html">热点05</a>
#     </ul>
# </div>
# '''
# html = etree.HTML(text)
# result = html.xpath('//li[1]/a/text()')
# print(result)
# result = html.xpath('//li[last()]/a/text()')
# print(result)
# result = html.xpath('//li[position()<3]/a/text()')
# print(result)
# result = html.xpath('//li[last()-2]/a/text()')
# print(result)


### 节点轴选择
from lxml import etree
text = '''
<div>
    <ul>
        <li class="item-0"><a href="link1.html"><span>首页01</span></a></li>
        <li class="item-1"><a href="link2.html">电影02</a></li>
        <li class="item-inactive"><a href="link3.html">影院03</a></li>
        <li class="item-0"><a href="link4.html">榜单04</a></li>
        <li class="item-1"><a href="link5.html">热点05</a>
    </ul>
</div>

<div><p></p></div>
'''
html = etree.HTML(text)
result = html.xpath('//li[1]/ancestor::*')   ###ancestor 获取祖先轴
print(result)
result = html.xpath('//li[1]/ancestor::div')
print(result)
result = html.xpath('//li[1]/attribute::*')   ###attribute 获取所有的属性轴
print(result)
# result = html.xpath('//li[1]/child::a[@href="link1.html"]')   ###child获取所有直接子节点
result = html.xpath('//li[1]/child::*')   ###child获取所有直接子节点
print(result)
result = html.xpath('//li[1]/descendant::span') ###descendant 获取所有的子孙节点
print(result)
# result = html.xpath('//li[1]/following::*[2]') ###following  获取当前节点之后的所有节点  *[2]  表示之后的所有节点中的第二个
result = html.xpath('//li[1]/following::*')   ###following  获取当前节点之后的所有节点
print(result)
result = html.xpath('//li[1]/following-sibling::*')   ###获取当前节点之后的所有的同级节点
print(result)
