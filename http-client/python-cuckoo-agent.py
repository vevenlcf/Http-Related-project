# -*- coding: utf-8 -*-
# 主要用于模拟 cuckoo客户端，与server端进行交互。server端采取的是cgi编程，而客户端主要是表单的一些使用方法
import requests
url = 'http://172.16.8.96:8888/store'
requests.adapters.DEFAULT_RETRIES =100
header = {'ENCTYPE':'multipart/form-data','User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'}
files = {'file': open('8.py', 'rb')} # 文件
data = {'filepath':'/tmp/tmp2.txt'}
r = requests.post(url, headers=header, files=files, data = data)


#抓包
""" 
POST /store HTTP/1.1
Host: 172.16.8.96:8888
Connection: keep-alive
Content-Length: 3950
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
Origin: null
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryslcBE6qynWxYLXGb
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cookie: wp-settings-time-1=1533565716

------WebKitFormBoundaryslcBE6qynWxYLXGb
Content-Disposition: form-data; name="file"; filename="tmp.txt"
Content-Type: text/plain

Generic hashes:
md5: 7b43567b4c32ad7aded537cd3b1342b9
sha1: 8322f1c2c355d88432f1f03a1f231f63912186bd
sha256: 050bbeb6b9aa404261b20989325c68433708367aaaed4e1dff3d24ae29a52d2a
sha512: f8c060cc3c2e44db4c040e7c9cfb05428a17920a27c44e258fe75d11e36ce656a7d01886e646fe8e1aa7b49a1659770c212ab4914942356506160d1fac6b1672

------WebKitFormBoundaryslcBE6qynWxYLXGb
Content-Disposition: form-data; name="filepath"

/tmp/tmp.txt
------WebKitFormBoundaryslcBE6qynWxYLXGb--
HTTP/1.0 200 OK
Server: Cuckoo Agent Python/2.7.5
Date: Fri, 14 Sep 2018 02:13:08 GMT

{"message": "Successfully stored file"}
"""
