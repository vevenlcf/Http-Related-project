# -*- coding: utf-8 -*-
#!/usr/bin/env python
# Python Network Programming Cookbook -- Chapter - 4
# This program is optimized for Python 2.7.
# It may run on any other version with/without modifications.
import urllib
import os
import sys

TARGET_URL = 'http://ufldl.stanford.edu/housenumbers/'
TARGET_FILE = 'test_32x32.mat'
file_total_size =64275384

class CustomURLOpener(urllib.FancyURLopener):
    def http_error_206(self, url, fp, errcode, errmsg, headers, data=None):
        pass

def resume_download():
    file_exists = False
    CustomURLClass = CustomURLOpener()
    if os.path.exists(TARGET_FILE):
        out_file = open(TARGET_FILE, "ab")
        file_exists = os.path.getsize(TARGET_FILE)
        # If the file exists, then only download the unfinished part
        CustomURLClass.addheader("range", "bytes=%s-" % (file_exists))
        print "bytes=%s-" % (file_exists)
    else:
        out_file = open(TARGET_FILE, "wb")

    web_page = CustomURLClass.open(TARGET_URL + TARGET_FILE)
    # Check if last download was OK
    # FILE_LENGTH 文件大小
    file_length = int(web_page.headers['Content-Length'])
    if file_exists >= file_total_size:
        loop = 0
        print "File download %d Bytes, remain size %d Bytes need download" % (file_exists, file_length)
        print "File already downloaded!"
        exit(1)
    else:
        print "File download %d Bytes, remain size %d Bytes need download" %(file_exists, file_length)

    byte_count = 0
    while True:
        data = web_page.read(4096)
        if not data:
            break
        out_file.write(data)
        byte_count = byte_count + len(data)
        out_file.flush()
        done = int((50*(byte_count + file_exists) / file_total_size))
        sys.stdout.write("\r[%s%s] %d%%" % ('█' * done, ' ' * (50 - done), 100 * (byte_count + file_exists) / file_total_size))
        sys.stdout.flush()


    web_page.close()
    out_file.close()
    for k, v in web_page.headers.items():
        print k, "=", v
    print "File copied", byte_count, "bytes from", web_page.url


if __name__ == '__main__':
    resume_download()