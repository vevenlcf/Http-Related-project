# -*- coding: utf-8 -*-
import sys
import requests
import os

TARGET_URL = 'http://ufldl.stanford.edu/housenumbers/'
TARGET_FILE = 'test_32x32.mat'
file_total_size =64275384

# 屏蔽warning信息，因为下面verify=False会报警告信息
requests.packages.urllib3.disable_warnings()


def download(url, file_path):
    headers = {}
    file_exists = 0
    if os.path.exists(file_path):
        out_file = open(file_path, "ab+")
        file_exists = os.path.getsize(file_path)
        # If the file exists, then only download the unfinished part
        ran = "bytes=" + str(file_exists) + "-"
        print ran
        headers = {"range":ran}
    else:
        out_file = open(file_path, "wb+")


    # verify=False 这一句是为了有的网站证书问题，为True会报错
    r = requests.get(url, headers = headers , stream=True, verify=False)

    # 既然要实现下载进度，那就要知道你文件大小啊，下面这句就是得到当前传输片段的大小
    file_size = int(r.headers['Content-Length'])
    print "current-size: %d" %(file_total_size)
    temp_size = 0

    with out_file as f:
        # iter_content()函数就是得到文件的内容，
        # 有些人下载文件很大怎么办，内存都装不下怎么办？
        # 那就要指定chunk_size=1024，大小自己设置，
        # 意思是下载一点写一点到磁盘。
        for chunk in r.iter_content(chunk_size=4096):
            if chunk:
                temp_size += len(chunk)
                f.write(chunk)
                f.flush()
                #############花哨的下载进度部分###############
                done = int(50 * (temp_size + file_exists) / file_total_size)
                # 调用标准输出刷新命令行，看到\r回车符了吧
                # 相当于把每一行重新刷新一遍
                sys.stdout.write("\r[%s%s] %d%%" % ('█' * done, ' ' * (50 - done), 100 * (temp_size + file_exists) / file_total_size))
                sys.stdout.flush()
    print()  # 避免上面\r 回车符，执行完后需要换行了，不然都在一行显示
    print r.headers

if __name__ == '__main__':
    # url是文件网址链接
    url = os.path.join(TARGET_URL, TARGET_FILE)
    # 调用上面下载函数即可
    download(url, TARGET_FILE)










