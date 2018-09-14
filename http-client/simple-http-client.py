# -*- coding: utf-8 -*-
# 主要用于模拟 simple-http-server的client 进行交互，主要header关键字‘refer’需要指定
import requests
url = 'http://172.16.8.96:8000'
header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
           'Cache-Control': 'max-age=0',
          'Origin': 'http://172.16.8.96:8000', 'Upgrade-Insecure-Requests': '1',
          'Accept': 'text / html, application / xhtml + xml, application / xml;q = 0.9, image / webp, image / apng, * / *;q = 0.8',
          'Referer': 'http: // 172.16.8.96:8000/', 'Accept-Encoding': 'gzip, deflate'}
files = {'file': open('30.py', 'rb')} # 文件
 # 其他表单
r = requests.post(url, headers=header, files=files)

