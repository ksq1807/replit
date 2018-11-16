# -*- coding: utf-8 -*-
import scrapy, json, re
from scrapy_redis.spiders import RedisSpider

# 普通的分布式
class GuaziSpider(RedisSpider):
    name = 'guazi'
    redis_key = 'guazi:start_urls'

    # 进行业务处理
    def parse(self, response):
        body = response.text.replace("\n","").replace("\t","").replace("\r","")
        info = re.findall('<a title=".*?" href="(.*?)"', body)
        if len(info)>0:
            for i in info:
                yield scrapy.Request(url="https://www.guazi.com%s"%i,callback=self.parse11)

    def parse11(self,response):
        body = response.text.replace("\n","").replace("\t","").replace("\r","")
        title = re.findall('class="titlebox">(.*?)<span',body)
        if len(title)>0:
            print(title[0])
        price = re.findall('class="pricestype">(.*?)<span', body)
        if len(price)>0:
            print(price[0])
        licheng = re.findall('class="assort clearfix">.*?"two"><span>(.*?)</span>', body)
        if len(licheng) > 0:
            print(licheng[0])
        print(response.url)








