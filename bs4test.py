#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-12-14 17:27:02
# @Author  : Yan Chen (cheny.gary@gmail.com)


from bs4 import BeautifulSoup
from webopener import getHtml
import time
import random
import re
from writeexcel import writeexcel



class Shop(object):
    """店铺信息类"""

    def __init__(self, shopn):

        __slots__ = ('sellern', 'main', 'credit', 'mnice', 'mmiddle', 'mbad')
        self.shopn = shopn


class Pagesoup(object):
    """解析网页内容的类"""

    def __init__(self, htmlcontent):

        self.htmlcontent = htmlcontent
        self.soupdata = BeautifulSoup(self.htmlcontent, 'html.parser')

    def sellername(self):
        div = self.soupdata.find_all(attrs={"class": "title"})
        return (div[0].contents[0].strip())

    def mainservice(self):
        div = self.soupdata.find("div", attrs={"class": "chart-main"})
        return(div.canvas['data-names'])

    def creditinfo(self):
        div = self.soupdata.find("div", attrs={"class": "list"})
        return(re.sub("\D", "", div.contents[0]))

    def mcreditok(self):
        div = self.soupdata.find_all("td", attrs={"class": "rateok"})
        try:
            return(div[1].a.contents[0])
        except:
            return(div[1].contents[0].strip())

    def mcreditnormal(self):
        div = self.soupdata.find_all("td", attrs={"class": "ratenormal"})
        try:
            return(div[1].a.contents[0])
        except:
            return(div[1].contents[0].strip())

    def mcreditbad(self):
        div = self.soupdata.find_all("td", attrs={"class": "ratebad"})
        try:
            return(div[1].a.contents[0])
        except:
            return(div[1].contents[0].strip())


if __name__ == "__main__":
    # with open('creditpage.html') as html:
    # 	soup = Pagesoup(html)
    # 	print(soup.mcreditbad())
    total = []
    total.append(['店名','卖家','主营','卖家信用','1月好评','1月中评','1月差评'])
    with open('shoplist.txt') as list:
        try:
            for line in list.readlines():
                time.sleep(random.uniform(5, 7))
                sname, surl = (line.split(","))
                html = getHtml(surl)
                tbshop = Shop(sname)
                soup = Pagesoup(html)

                tbshop.sellern = soup.sellername()
                tbshop.main = soup.mainservice()
                tbshop.credit = soup.creditinfo()
                tbshop.mnice = soup.mcreditok()
                tbshop.mmiddle = soup.mcreditnormal()
                tbshop.mbad = soup.mcreditbad()
                tbshoplist= [sname,tbshop.sellern,tbshop.main,tbshop.credit,tbshop.mnice,tbshop.mmiddle,tbshop.mbad]
                total.append(tbshoplist)


        except IndexError as e:
            print('抓了%d个' %(len(total)-1))
    if len(total) > 1:
        writeexcel('北美代购商家列表.xlsx', total)
    else:
        print('什么都抓不到')
