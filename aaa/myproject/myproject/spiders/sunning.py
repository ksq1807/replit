# -*- coding: utf-8 -*-
import scrapy, json, re
from myproject.items import MyprojectItem,Goods
from lxml import etree
from myproject.utils import send_email


class SunningSpider(scrapy.Spider):
    name = 'sunning'
    hearer = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36"
    }
    start_urls = [
        'https://www.suning.com/'
            ]
    # 进行业务处理
    def parse(self, response):
        body = response.xpath("//div[@class='title']")
        for i in body:
            # goods = Goods()
            if i.xpath("h5/text()").extract_first() != None:
                if i.xpath("a/@href").extract_first() != None:
                    goods={}
                    goods["title"] = i.xpath("h5/text()").extract_first()
                    goods["url"] = i.xpath("a/@href").extract_first()
                    print(goods)
                    # send_email.send_email("kousq_kousq@163.com","961094263@qq.com","爬虫","5sendeamil",goods["title"])
                    yield scrapy.Request(url=goods["url"],headers=self.hearer,callback=self.parse1)

    def parse1(self,reponse):
        print(111)
        body = reponse.xpath("//head/title/text()")
        print(222)

        print(body)













