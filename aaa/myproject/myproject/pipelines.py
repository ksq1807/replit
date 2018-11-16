# -*- coding: utf-8 -*-
import pymongo, pymysql
from myproject.items import MyprojectItem, LagouItem, GuaziItem, GzItem, News, Goods
from myproject import settings
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# 将item中得到的数据做入库处理
class MyprojectPipeline(object):
    def __init__(self):
        # 创建一个连接，用于连接到数据库
        # client = pymongo.MongoClient()
        client = pymongo.MongoClient(host=settings.MONGOHOST, port=settings.MONGOPORT)
        # 指定数据库的名字，支持字典或是列表
        # self.db = client.zhilian1030
        self.db = client[settings.MONGODB]

    def process_item(self, item, spider):
        table = ""
        if isinstance(item,MyprojectItem):
            # 创建一个表
            table = self.db.zhilian
        elif isinstance(item,LagouItem):
            # 创建一个表
            table = self.db.lgtable
        elif isinstance(item,GuaziItem):
            table = self.db.gztable
        elif isinstance(item, GzItem):
            table = self.db.guazi
        elif isinstance(item, News):
            table = self.db.ggzy
        elif isinstance(item, Goods):
            table = self.db.goods
        # 插入数据
        table.insert_one(dict(item))
        # print(item)
        return item

# 可以连接到MySQL数据库
# class Myproject333Pipeline(object):
#     def __init__(self):
#         # 创建一个连接，用于连接到数据库
#         self.connect = pymysql.connect(
#             host = "localhost",
#             prot = 3306,
#             db = "", # 数据库名称
#             user = "root",
#             password = "",
#             charset = "utf8"
#         )
#         self.coursor = self.connect.coursor()
#
#
#     def process_item(self, item, spider):
#         # 插入数据
#         self.coursor.execute(
#             "insert into bbb (item)"
#
#
#             """
#             insert into tablename (ziduan) VALUES (%s, %s)
#             """
#         )
#         # 提交数据
#         self.connect.commit()

class MysqlPipeline(object):
    def __init__(self):
        # 连接到数据库
        self.conn = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='',
            db='数据库名',
            charset='utf8'  # 编码格式
        )
        self.cur = self.conn.cursor()  # 游标

    # 业务处理
    def process_item(self, item, spider):
        try:
            # 插入数据，例子
            self.cur.execute(
                """insert into doubanmovie(name, info, rating, num ,quote, img_url)
                value (%s, %s, %s, %s, %s, %s)""",
                (item['name'],
                 item['info'],
                 item['rating'],
                 item['num'],
                 item['quote'],
                 item['img_url']))

            # 提交sql语句
            self.conn.commit()
            self.cur.close()  # 关闭游标
            self.conn.close()  # 关闭数据库
        except Exception as error:
            # 出现错误时打印错误日志
            print(error)
        return item

