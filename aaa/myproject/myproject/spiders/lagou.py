# -*- coding: utf-8 -*-
import scrapy, json, re
from myproject.items import LagouItem


class LagouSpider(scrapy.Spider):
    name = 'lagou'

    head = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        # "Content-Length": "26",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Host": "www.lagou.com",
        "Origin": "https://www.lagou.com",
        "Referer": "https://www.lagou.com/jobs/list_python?city=%E5%85%A8%E5%9B%BD&cl=false&fromSearch=true&labelWords=&suginput=",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
        "X-Anit-Forge-Code": "0",
        "X-Anit-Forge-Token": "None",
        "X-Requested-With": "XMLHttpRequest",
    }
    def start_requests(self):

        urls = ['https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false']
        data = {"first": "true",
                "pn": "1",
                "kd": "python"}
        for url in urls:
            yield scrapy.FormRequest(url=url, formdata=data, headers=self.head,callback=self.parse)

    def parse(self, response):
        jsondata = json.loads(response.text)
        data = jsondata["content"]["positionResult"]["result"]
        for item in data:
            lgitem = LagouItem()
            lgitem["companyName"] = item["companyFullName"]
            lgitem["salary"] = item["salary"]
            lgitem["jobname"] = item["positionName"]
            url = "https://www.lagou.com/jobs/%s.html" % (item["positionId"])
            yield scrapy.Request(url=url, callback=self.parse11, meta={"lgitem": lgitem}, headers=self.head)

    def parse11(self,response):
        # 接收上面传来的数据
        lgitem = response.meta["lgitem"]
        body = response.text.replace("\n","")
        gwzz =re.findall('class="job_bt">(.*?)</dd>', body)
        if len(gwzz)>0:
            lgitem["gwms"] = gwzz[0]
        yield lgitem




