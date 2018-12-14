# 抓取猫眼电影排行
import requests
from requests.exceptions import RequestException
import re
import json
import time


def get_one_page(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            response.encoding = "gbk"
            return response.text
        return None
    except RequestException:
        return None

def parse_one_page(html):
    pattern = re.compile('<tr>.*?first tc.*?>(.*?)</td>'
                         '.*?href="(.*?)".*?>(.*?)</a></td>'
                         '.*?J_showCanvas.*?>(.*?)</a></td>'
                         '.*?td>(.*?)</td>'
                         '.*?c-rise.*?>(.*?)</td>'
                         '.*?tr.*?>(.*?)</td>'
                         '.*?tr.*?>(.*?)</td>'
                         '.*?tr.*?>(.*?)</td>'
                         '.*?c-fall.*?>(.*?)</td>'
                         '.*?tr.*?>(.*?)</td>'
                         '.*?tr.*?>(.*?)</td>'
                         '.*?</tr>'
                         ,re.S)
                         # '.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>'
                         # '.*?star.*?>(.*?)</p>'
                         # '.*?releasetime.*?>(.*?)</p>'
                         # '.*?integer.*?>(.*?)</i>'
                         # '.*?fraction.*?>(.*?)</i>', re.S)
    items = re.findall(pattern, html)
    print(items)
    # for item in items:
    #     yield {
    #         'index': item[0],
    #         'image': item[1],
    #         'title': item[2].strip(),
    #         'actor': item[3].strip()[3:],
    #         'time': item[4].strip()[5:],
    #         'score': item[5].strip() + item[6].strip()
    #     }


def write_to_file(content):
    with open('result.txt', 'a', encoding='utf-8') as f:
        print(json.dumps(content))
        f.write(json.dumps(content, ensure_ascii=False) + '\n')

def main():
    url = 'http://data.10jqka.com.cn/funds/ggzjl/'
    html = get_one_page(url)
    parse_one_page(html)
    # print(html)
    # print('#'*100)
    # for item in parse_one_page(html):
    #     print(item)
    #     write_to_file(item)
        
if __name__ == '__main__':
    # for i in range(10):
    #     main(offset=i * 10)
    #     time.sleep(1)
    main()