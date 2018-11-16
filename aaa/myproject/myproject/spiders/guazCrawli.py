# -*- coding: utf-8 -*-
import scrapy, json, re
from myproject.items import MyprojectItem,GuaziItem,GzItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy_redis.spiders import RedisCrawlSpider

# 深度爬取，定制的方法，不是分布式
class GuaziSpider(CrawlSpider):
    name = 'guazcrawl'
    start_urls = ['https://www.guazi.com/sjz/dazhong/']
    # header = {  # 默认的请求头
    #     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    #     # "Accept-Encoding": "gzip, deflate, br",
    #     "Accept-Language": "zh-CN,zh;q=0.9",
    #     "Connection": "keep-alive",
    #     "Cookie": "antipas=31Ih4kdM73426Q99z3F56yJ5035;",
    #     "Host": "www.guazi.com",
    #     "Referer": "https://www.guazi.com/sjz/dazhong/",
    #     "Upgrade-Insecure-Requests": "1",
    #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36"
    # }
    rules = (
        # 用于提取下一页的地址，同一个页面下拿取数据
        Rule(LinkExtractor(allow=('/sjz/dazhong/o2/#bread',))),
        # 用于提取具体的连接
        Rule(LinkExtractor(allow=('/sjz/\w{17}\.htm#fr_page=list&fr_pos=city&fr_no=\d+',)), callback='parse_item'),
    )

    # 回调函数
    def parse_item(self, response):
        # 初始化数据库
        guazi = GzItem()
        # 得到页面的数据
        body = response.text.replace("\n","").replace("\r","").replace("\t","")
        # 使用正则进行匹配
        title = re.findall('class="titlebox">(.*?)<span', body)
        if len(title)>0:
            guazi["name"] = title[0]
        price = re.findall('class="pricestype">(.*?)<span', body)
        if len(price)>0:
            guazi["price"] = price[0]
        licheng = re.findall('class="assort clearfix">.*?"two"><span>(.*?)</span>', body)
        if len(licheng)>0:
            guazi["licheng"] = licheng[0]
        guazi["url"] = response.url
        yield guazi







