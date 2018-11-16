# -*- coding: utf-8 -*-
import scrapy, json, re
from myproject.items import MyprojectItem,GuaziItem


class GuaziSpider(scrapy.Spider):
    name = 'guazi2'
    header = {  # 默认的请求头
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        # "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Cookie": "antipas=31Ih4kdM73426Q99z3F56yJ5035;",
        "Host": "www.guazi.com",
        "Referer": "https://www.guazi.com/sjz/dazhong/",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36"
    }
    # 连接到url，得到网页源代码，并使用回调函数执行相应的业务
    def start_requests(self):

        urls = [
            'https://www.guazi.com/sjz/dazhong/',
        ]
        for url in urls:
            # 进入到回调函数
            yield scrapy.Request(url=url, headers=self.header, callback=self.parse)
    # 进行业务处理
    def parse(self, response):
        body = response.text.replace("\n","").replace("\t","").replace("\r","")
        info = re.findall('<a title=".*?" href="(.*?)"', body)
        if len(info)>0:
            for i in info:
                yield scrapy.Request(url="https://www.guazi.com%s"%i,headers=self.header,callback=self.parse11)

    def parse11(self,response):
        myitem = GuaziItem()
        body = response.text.replace("\n","").replace("\t","").replace("\r","")
        title = re.findall('class="titlebox">(.*?)<span',body)
        if len(title)>0:
            myitem["title"] = title[0]
        price = re.findall('class="pricestype">(.*?)<span', body)
        if len(price)>0:
            myitem["price"] = price[0]
        licheng = re.findall('class="assort clearfix">.*?"two"><span>(.*?)</span>', body)
        if len(licheng) > 0:
            myitem["licheng"] = licheng[0]
        yield myitem








