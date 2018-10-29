#################################文本文件
#######  写入文件
# import requests
# from pyquery import PyQuery as pq
#
# url = 'https://www.zhihu.com/explore'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'
# }
# html = requests.get(url, headers=headers).text
# doc = pq(html)
# items = doc('.explore-tab .feed-item').items()
# print(items)
# for item in items:
#     question = item.find('h2').text()
#     author = item.find('.author-link-line').text()
#     answer = pq(item.find('.content').html()).text()
#     with open('explore.txt', 'a', encoding='utf-8') as file:
#         file.write('\n'.join([question, author, answer]))
#         file.write('\n' + '=' * 50 + '\n')
#     # file = open('explore.txt', 'a', encoding='utf-8')
#     # file.write('\n'.join([question, author, answer]))
#     # file.write('\n' + '=' * 50 + '\n')
#     # file.close()

########### json
# import json
#
# str = '''
# [{
#     "name": "Bob",
#     "gender": "male",
#     "birthday": "1992-10-18"
# },
# {
#     "name": "张三",
#     "gender": "femal",
#     "birthday": "1995-10-18"
# }]
# '''
# print(type(str))
# data = json.loads(str)
# print(data)
# print(type(json))
#
# print(data[0]['name'])
# print(data[0].get('name'))
#
#
# print(data[0].get('age'))
# print(data[0].get('age', 25))  ##  获取不到后面的填充


#####  输出json
# data = json.loads(str)
# with open('data.json', 'w') as file:
#     # file.write(json.dumps(data))   ##无格式保存
#     # file.write(json.dumps(data, indent=2))   ## indent代表缩进字符
#     file.write(json.dumps(data, indent=2, ensure_ascii=False)) ### 表示中文字符是否输出编码 默认输出编码


############################CSV文件存储
##基本写入
import csv

# with open('data.csv', 'w') as csvfile:
#     # writer = csv.writer(csvfile)
#     writer = csv.writer(csvfile, delimiter=' ') ###修改分隔符
#     writer.writerow(['id', 'name', 'age'])
#     # writer.writerow(['10001', 'Mike', 20])
#     # writer.writerow(['10002', 'Bob', 21])
#     # writer.writerow(['10003', 'Jorban', 22])
#     writer.writerows([['10001', 'Mike', 20],['10003', 'Jorban', 22]])  ## 一下写入多行  传入二维

# ##字典写入模式
# with open('data.csv', 'w') as csvfile:
#     fieldnames = ['id', 'name', 'age']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writerow({'id': '1001', 'name': 'Mike', 'age': 20})
#
# #### 字典追加写
# with open('data.csv', 'a') as csvfile:
#     fieldnames = ['id', 'name', 'age']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     writer.writerow({'id': '1002', 'name': 'Bob', 'age': 21})

### csv读取
# import csv
#
# with open('data.csv', 'r', encoding='utf-8') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)

##使用pandas读取csv
import pandas as pd

df = pd.read_csv('data.csv')
print(df)
