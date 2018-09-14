#!/bin/bash
###默认的python cgi服务 能够列出当前目录所有文件 
cd /tmp
python -m CGIHTTPServer 8080
