# -*- coding=utf-8 -*- 
import urllib2
import socket
import time

urls = raw_input("Please enter a web address: \n> ")
print "\nAccess web page start.",
time.sleep(1)
print ".",
time.sleep(1)
print "."
brushNum = 3600
for i in range(brushNum):
    url = urls
    #socket.setdefaulttimeout
    req_header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept':'text/html;q=0.9,*/*;q=0.8',
    'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding':'gzip',
    'Connection':'close',
    'Referer':None 
    }
    req_timeout = 180
    try: #try用法
        req = urllib2.Request(url,None,req_header)
        resp = urllib2.urlopen(req,None,req_timeout)
        html = resp.read()
        print "Success! >>>",i + 1
        print "Rest 10 seconds to continue.",
        time.sleep(1)
        print ".",
        time.sleep(1)
        print "."
        print "================================"
        time.sleep(10)
    except : #发现错误，处理
        print "We failed to reach a server."
    else: #没有错误
        print "No exception was raised."
