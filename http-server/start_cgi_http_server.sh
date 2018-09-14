#!/bin/bash

mkdir ./cgi-bin/
cp upload.cgi ./cgi-bin/
chmod +x ./cgi-bin/upload.cgi
mkdir ./upload/
python -m CGIHTTPServer 8080
