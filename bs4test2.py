#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-12-15 13:43:44
# @Author  : Yan Chen (cheny.gary@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import urllib.request
import urllib.parse
import json
from webopener import getHtml
from bs4 import BeautifulSoup
import re


if __name__ == "__main__":
    # keyword = input("请输入关键字")
    with open('shoplist.txt', 'w') as shoplist:
		    for pagecount in range(0, 2000, 20):
		        postdata = {
		            'q': '北美代购',
		            'js': '1',
		            'ie': 'utf8',
		            'sort': 'credit-desc',
		            's': pagecount
		        }
		        postdata = urllib.parse.urlencode(postdata)
		        tburl = "https://shopsearch.taobao.com/search?app=shopsearch&" + postdata

		        try:
		            content1 = getHtml(tburl)
		            content1 = content1.decode('utf-8', 'ignore')
		            content1 = re.findall(
		                r'g_page_config = (.*?);\n', content1, re.S)
		            shop = json.loads(content1[0])
		            shopfiles = shop['mods']['shoplist']['data']['shopItems']
		            for shopfile in shopfiles:
		                shopinfo = shopfile['title'] + ',' + 'https://' + \
		                    re.sub(r'//(.*?)', '', shopfile['userRateUrl'])+'\n'
		                shoplist.write(shopinfo)

		        except Exception as e:
		            if hasattr(e, 'code'):
		                print('页面不存在或时间太长.')
		                print('Error code:', e.code)
		            elif hasattr(e, 'reason'):
		                print("无法到达主机.")
		                print('Reason:  ', e.reason)
		            else:
		                print(e)

