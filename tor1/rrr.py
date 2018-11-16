from peewee import *
#
# # db = SqliteDatabase('people.db')
# db = MySQLDatabase("mysql+pool://root:123456@127.0.0.1:33888/sss?max_connections=300&stale_timeout=300")
# # db.connect()
#
# class Person(Model):
#     name = CharField()
#     birthday = DateField()
#
#     class Meta:
#         database = db  # This model uses the "people.db" database.
#
# Person.create_table()
#
# import peewee
# from peewee import *
# db = MySQLDatabase('sss', user='root', passwd='123456',port=33888)
# class Book(peewee.Model):
#   author = peewee.CharField()
#   title = peewee.TextField()
#   class Meta:
#     database = db
# Book.create_table()
# book = Book(author="me", title='Peewee is cool')
# book.save()
# for book in Book.filter(author="me"):
#   print(book.title)
from datetime import datetime
from  pymongo import *
from decimal import Decimal

db = MySQLDatabase('sss',
                   host='127.0.0.1',
                   user='root',
                   passwd='123456',
                   charset='utf8',
                   port=33888
                   )

db.connect()


class User(Model):
    username = CharField()
    password = CharField()

    class Meta:
        database = db  # T

# User.create_table()
u=User()
u.username="123"
u.password="3445"
u.save()
# cur = db.execute_sql('show tables')
# ccc= cur.fetchall()
# print('d')
