# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

# 提取，定义要爬取的字段
class MyprojectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    salary = scrapy.Field()
    jobName = scrapy.Field()
    companyName = scrapy.Field()
    gwms = scrapy.Field()


class LagouItem(scrapy.Item):
    salary = scrapy.Field()
    jobname = scrapy.Field()
    companyName = scrapy.Field()
    gwms = scrapy.Field()


class GuaziItem(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()
    licheng = scrapy.Field()


class GzItem(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    licheng = scrapy.Field()
    url = scrapy.Field()


class News(scrapy.Item):
    title = scrapy.Field()
    times = scrapy.Field()
    words = scrapy.Field()
    url = scrapy.Field()



class Goods(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()
    url = scrapy.Field()