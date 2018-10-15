'''
抓取猫眼的电影排行
访问地址：
    http://maoyan.com/board/4

使用requests进行抓取
'''

import re

import requests


def get_one_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743 Safri/537.36'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    return None

def parse_on_page(html):
    pattern = re.compile('<dd>.*board-index-.*">(\d+)</i>', re.S)
    # pattern = re.compile('<dd>.*?board-index.*?>(.*?)</i>', re.S)
    data = re.findall(pattern, html)
    print(data)

def main():
    url = 'http://maoyan.com/board/4'
    html = get_one_page(url)
    print(html)
    parse_on_page(html)


if __name__ == '__main__':
    main()