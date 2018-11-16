# -*- coding: utf-8 -*-
import scrapy, json, re
from myproject.items import MyprojectItem


class ZhilianSpider(scrapy.Spider):
    name = 'zhilian'
    # 连接到url，得到网页源代码，并使用回调函数执行相应的业务
    def start_requests(self):
        urls = [
            'https://fe-api.zhaopin.com/c/i/sou?pageSize=60&cityId=489&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=python&kt=3&lastUrlQuery=%7B%22jl%22:%22489%22,%22kw%22:%22python%22,%22kt%22:%223%22%7D&_v=0.41798019&x-zp-page-request-id=056d9865a18144338fb1b0a70d253dd1-1540893442786-28426',
        ]

        for url in urls:
            # 进入到回调函数
            yield scrapy.Request(url=url, callback=self.parse)
    # 进行业务处理
    def parse(self, response):
       jsondata = json.loads(response.text)
       result = jsondata["data"]["results"]
       for item in result:
           # 初始化数据库的链接,用于保存数据
           myitem = MyprojectItem()
           # 需要继续爬取的对象
           deurl = item["positionURL"]
           # 要保存的数据
           myitem["salary"] = item["salary"]
           myitem["jobName"] = item["jobName"]
           myitem["companyName"] = item["company"]["name"]
           # 异步请求
           # 数据入库处理，yield把要做的工作交还给引擎
           yield myitem
           # 有下一级的url时，继续向下挖掘
           yield scrapy.Request(deurl, callback=self.parse22, meta={"istem": myitem})
    def parse22(self,reponse):
        myitem = reponse.meta["istem"]
        body = reponse.text.replace("\n","")
        info = re.findall('class="pos-ul">(.*?)<div>',body)
        # 初始化
        # myitem = GwzzItem()
        if len(info)>0:
            myitem["gwms"] = info[0]
            yield myitem
