#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-12-14 16:35:55
# @Author  : Yan Chen (cheny.gary@gmail.com)

from html.parser import HTMLParser
from urllib import request
import os

class Myparaser(HTMLParser):
	def handle_starttag(self, tag, attrs):
		print ('Encounter a start tag', tag)

	def handle_endtag(self, tag):
		print('Encounter a end tag', tag)

	def handle_data(slef,data):
		print('Encounter data', data)

# paraser = Myparaser()
# paraser.feed('''<html>
# <head></head>
# <body>
# <!-- test html parser -->
#     <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
# </body></html>''')



with request.urlopen('https://rate.taobao.com/user-rate-UvGNYvGgLOmku.htm?spm=a230r.7195193.1997079397.3.ZsZZtG') as f:
    data = f.read()
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', data.decode('GBK'))