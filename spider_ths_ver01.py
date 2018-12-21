import requests
import re
class THS:
    def __init__(self):
        self.base_url ='http://data.10jqka.com.cn/funds/ggzjl/field/zdf/order/desc/page/{}/ajax/1/'
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
                        "X-Requested-With":"XMLHttpRequest",
                        "Host": "data.10jqka.com.cn",
                        "Referer":"http://data.10jqka.com.cn/funds/ggzjl/",
                         "Accept":"text/html, */*; q=0.01",
                         "Accept-Encoding": "gzip, deflate",
                         "Accept-Language": "zh-CN,zh;q=0.9",
                         "hexin-v": "AtJ5zcQo2nGawSaNaMrs57sKI5O349ZkCObKoZwr_C5wpnwFhHMmjdh3GrNv"
                        }

    def get_url_list(self):
        url_list = []
        for page in range(2):
            url_list.append(self.base_url.format(page+1))
        return  url_list

    def parase_html_data(self,html):
        pattern = re.compile('<tr.*?first tc.*?>(.*?)</td>'  # 序号
                             '.*?href="(.*?)".*?>(.*?)</a></td>'  # 股票代码
                             '.*?J_showCanvas.*?>(.*?)</a></td>'  # 股票简称
                             '.*?td>(.*?)</td>'  # 最新价
                             '.*?td.*?>(.*?)</td>'  # 涨跌幅
                             '.*?td.*?>(.*?)</td>'  # 换手率
                             '.*?td.*?>(.*?)</td>'  # 流入资金
                             '.*?td.*?>(.*?)</td>'  # 流出资金
                             '.*?td.*?>(.*?)</td>'  # 净额
                             '.*?td.*?>(.*?)</td>'  # 成交额
                             '.*?td.*?>(.*?)</td>'  # 大单流入
                             '.*?</tr>'
                             , re.S)

        data_format_result = re.findall(pattern, html)
        # for data in data_format_result:
        #     yield {
        #         'code': data[0],
        #         'codename': data[1],
        #         'zxj': data[2].strip(),
        #         'zdf': data[3].strip(),
        #         'hsl': data[4].strip(),
        #         'flowin': data[5].strip(),
        #         'flowout': data[6].strip(),
        #         'zjjlr': data[7].strip(),
        #         'money': data[8].strip(),
        #         'ddlr': data[9].strip(),
        #     }

        return data_format_result

    def run(self):
        # 1. 构造url
        url_list = self.get_url_list()
        # 2. 发送请求
        data_list = []
        for url in url_list:
            response = requests.get(url,headers = self.headers)
            data_list.append(self.parase_html_data(response.content.decode("gbk")))
        return data_list


        # 3. 保存结果

if __name__=='__main__':
    ths = THS()
    rs = ths.run()
    print(rs)