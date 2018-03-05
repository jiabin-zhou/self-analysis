# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
# import sqlite3
import pymysql

class TutorialPipeline(object):
    def open_spider(self,spider):
        #链接数据库
        self.conn=pymysql.connect(host='localhost',
                                  port=3306,
                                  db='mysql_test',
                                  user='root',
                                  password='root',
                                  charset='utf8')
        #创建游标
        self.cursor=self.conn.cursor()
    def close_spider(self,spider):
        #关闭数据库链接
        self.conn.close()
    def process_item(self, item, spider):
        #向数据库data表中新增数据
        insert="insert into test1 (appid,date,count,rate) VALUES ('{}','{}','{}','{}')".format(item['appid'],item['date'],item['count'],item['rate'])
        print(insert)
        cursor=self.cursor.execute(insert)
        #提交事务！
        self.conn.commit()
        return item

# class TutorialPipeline(object):
#     def open_spider(self,spider):
#         #链接数据库
#         self.conn=sqlite3.connect('data.sqlite')
#         #创建游标
#         self.cursor=self.conn.cursor()
#     def close_spider(self,spider):
#         #关闭数据库链接
#         self.conn.close()
#     def process_item(self, item, spider):
#         #向数据库data表中新增数据
#         insert="insert into data (appid,date, count, rate) VALUES ('{}','{}','{}','{}')".format(item['appid'],item['date'],item['count'],item['rate'])
#         print(insert)
#         cursor=self.cursor.execute(insert)
#         #提交事务！
#         self.conn.commit()
#         return item
