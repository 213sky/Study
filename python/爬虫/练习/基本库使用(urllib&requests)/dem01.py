'''
抓取猫眼的电影排行
访问地址：
    http://maoyan.com/board/4

使用requests进行抓取
'''
import json
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
    pattern = re.compile('<dd>.*?board-index-.*?>(.*?)</i>'
                         '.*?data-src="(.*?)"'
                         '.*?alt="(.*?)"'
                         '.*?class="star">(.*?)</p>'
                         '.*?releasetime">(.*?)</p>'
                         '.*?class="integer">(.*?)</i>'
                         '.*?class="fraction">(.*?)</i>', re.S)
    data = re.findall(pattern, html)
    for item in data:
        yield {
            'index': item[0],
            'image': item[1],
            'title': item[2].strip(),
            'actor': item[3].strip()[3:] if len(item) > 3 else '',
            'time': item[4].strip()[5:] if len(item) > 5 else '',
            'score': item[5] + item[6]
        }

def write_to_file(content):
    with open('result.txt', 'a', encoding='utf-8') as f:
        # print(type(json.dumps(content)))
        f.write(json.dumps(content, ensure_ascii=False) + '\n')

def main(offset):
    url = 'http://maoyan.com/board/4?offset=' + str(offset)
    html = get_one_page(url)
    # print(html)
    ss = parse_on_page(html)
    for s in ss:
        write_to_file(s)


if __name__ == '__main__':
    for i in range(11):
        main(i * 10)