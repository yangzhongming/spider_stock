import requests
import re

class Hexun:
    def __init__(self):
        self.date = '2018-12-20_14:30:00'
        self.base_url = 'http://focus.stock.hexun.com/service/stock_sort_xml.jsp?date={}&type=1&start={}&count=20'
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'"}

    def get_url_list(self):
        url_list = []
        for start in range(1):
            url_list.append(self.base_url.format(self.date,start*20))
            print(url_list)
        return url_list

    def parse_url(self,url):
        print(url)
        response = requests.get(url,headers=self.headers)
        print('#' * 100)
        print(response.content.decode('gb2312'))
        print('#' * 100)
        strtemp = response.content.decode('gb2312')
        print(strtemp)
        stokcs = self.str_format(strtemp)
        for i in stokcs:
            print(i)
        return response.content.decode('gb2312')

    def str_format(self,stocks):
        print("str_format start:")

        pattern = re.compile('<sortid>(.*?)</sortid>'
                             '<code>(.*?)</code>'
                             '<name>(.*?)</name>'
                             '<rate>(.*?)</rate>'
                             '<change>(.*?)</change>'
                             '<changerate>(.*?)</changerate>'
                             '<sortidchange>(.*?)</sortidchange>'
                             '<price>(.*?)</price>'
                             , re.S)
        str_format_result = re.findall(pattern,stocks)
        print(str_format_result)

        for item in str_format_result:
            yield {
                'sortid': item[0],
                'code': item[1],
                'name':  item[2],
                'rate': item[3],
                'change': item[4],
                'changerate': item[5],
                'sortidchange': item[6],
                'price': item[7]
            }




        print("str_format end:")
        return str_format_result

    def run(self):
        # 1.构造url列表
        url_list = self.get_url_list()
        # 2.遍历，发送请求，获取响应
        for url in url_list:
            stocks = self.parse_url(url)
        # 3. 保存结果


if __name__== '__main__':
    hexun = Hexun()
    hexun.run()