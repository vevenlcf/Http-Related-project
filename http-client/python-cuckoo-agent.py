# -*- coding: utf-8 -*-
import requests
url = 'http://172.16.8.96:8888/store'
requests.adapters.DEFAULT_RETRIES =100
header = {'ENCTYPE':'multipart/form-data','User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'}
files = {'file': open('8.py', 'rb')} # 文件
data = {'filepath':'/tmp/tmp2.txt'}
r = requests.post(url, headers=header, files=files, data = data)
