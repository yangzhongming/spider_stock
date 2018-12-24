import requests
import re
import json

class EastMoney:
    def __init__(self):
        self.base_url ='http://nufm.dfcfw.com/EM_Finance2014NumericApplication/JS.aspx?'
        self.headers={
            "Cache-Control": "private",
            "Connection": "close",
            "Content-Encoding": "gzip",
            "Content-Type": "text/plain;charset = utf - 8",
            "Date": "Mon, 24 Dec 2018 03: 20:33 GMT",
            "Server": "Microsoft-IIS/7.5",
            "Vary": "Accept-Encoding",
            "X-AspNet-Version": "4.0.30319"
        }
        self.params = {
                        "type":"ct",
                        "st": "(BalFlowMain)",
                        "sr": "-1",
                        "p": "1",
                        "ps": "50",
                        "js": 'var AUUzAKjz={pages:(pc),date:"2014-10-22",data:[(x)]}',
                        "token":"894050c76af8597a853f5b408b759f5d",
                        "cmd": "C._AB",
                        "sty": "DCFFITA",
                         "rt": "51520907"
                        }

    def get_url_list(self):
        url_list = []
        for page in range(5):
            url_list.append(self.base_url.format(page+1))
            # print(url_list)
        return  url_list

    def get_data(self,response):
        pattern = re.compile('{.*?}',re.S)
        data_result = re.findall(pattern,response)
        print(data_result)

        return  data_result


    def run(self):
        # 1. 发送请求
        response = requests.get(self.base_url, params=self.params)
        print(response.content.decode())
        # 2. 提取数据
        data_result = self.get_data(response.content.decode())
        return data_result

if __name__=='__main__':
    eastMoney = EastMoney()
    rs = eastMoney.run()
