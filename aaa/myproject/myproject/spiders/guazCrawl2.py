# -*- coding: utf-8 -*-
import scrapy, json, re
from myproject.items import MyprojectItem,GuaziItem,GzItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy_redis.spiders import RedisCrawlSpider

# 深度爬取，定制的方法，用于分布式爬取
class GuaziSpider(RedisCrawlSpider):
    name = 'guazcrawl333'
    redis_key = 'guazcrawl333:start_urls'

    rules = (
        # 用于提取下一页的地址，同一个页面下拿取数据
        Rule(LinkExtractor(allow=('/sjz/dazhong/o\d+/#bread',))),
        # 用于提取具体的连接
        Rule(LinkExtractor(allow=('/sjz/\w{17}\.htm#fr_page=list&fr_pos=city&fr_no=\d+',)), callback='parse_item'),
    )

    # 业务处理
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







