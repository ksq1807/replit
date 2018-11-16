# -*- coding: utf-8 -*-
import scrapy, json, re
from myproject.items import LagouItem, News
from lxml import etree
from bs4 import BeautifulSoup


class LagouSpider(scrapy.Spider):
    name = 'yhggzy'

    def start_requests(self):
        urls = ['http://www.yhggzy.com.cn/Module/ModuleView.aspx?ModuleID=295&ViewID=317']
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)

    def parse(self, response):
        body = response.text.replace("\n","").replace("\t","").replace("\r","")
        soup = BeautifulSoup(body, 'lxml')
        data = soup.find_all("td", class_="DispLimitColumn")
        new = News()
        for i in data:
            new["title"] = i.parent.contents[1].text
            new["url"] = "http://www.yhggzy.com.cn/ProArticle/" + i.parent.contents[1].contents[1].contents[1].attrs["href"]
            new["time"] = i.parent.contents[4].text





    def parse11(self,response):
        pass







