'''
头条下载最新的  街拍图片
唯一缺点下载的都是小图片
'''
import requests
from urllib.parse import urlencode
import os
from hashlib import md5
from multiprocessing.pool import Pool

url_base = 'https://www.toutiao.com/search_content/?'

def get_page(offset):
    params = {
        'offset': offset,
        'format': 'json',
        'keyword': '街拍',
        'autoload': 'true',
        'count': '20',
        'cur_tab': '1',
        'from': 'search_tab'
    }
    url = url_base + urlencode(params)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError:
        return None

def get_images(json):
    if json.get('data'):
        for item in json.get('data'):
            title = item.get('title')
            images = item.get('image_list')
            if images is None:
                continue
            for image in images:
                yield{
                    'image': image.get('url'),
                    'title': title
                }

def save_image(item):
    if not os.path.exists(item.get('title')):
        os.mkdir(item.get('title'))
    try:
        url = 'http:' + item.get('image')
        response = requests.get(url)
        if response.status_code == 200:
            file_path = '{0}/{1}.{2}'.format(item.get('title'), md5(response.content).hexdigest(), 'jpg')
            if not os.path.exists(file_path):
                with open(file_path, 'wb') as f:
                    f.write(response.content)
            else:
                print('Already DownLoaded', file_path)
    except requests.ConnectionError:
        print('Failed to Save Image')
    except Exception as e:
        print(e)


def main(offset):
    json = get_page(offset)
    for item in get_images(json):
        print(item)
        save_image(item)

GROUP_START = 1
GROUP_END = 20

if __name__ == '__main__':
    pool = Pool()
    groups = ([x * 20 for x in range(GROUP_START, GROUP_END + 1)])
    pool.map(main, groups)
    pool.close()
    pool.join()




