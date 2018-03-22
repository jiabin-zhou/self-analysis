# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem
import redis
import scrapy_redis_mysql.settings as settings
import pymysql
import datetime

class redis_Pipeline(object):
    def __init__(self):
        self.redis_table = settings.MY_REDIS  # 选择表
        self.redis_db = redis.Redis(host=settings.REDIS_SERVER, port=settings.REDIS_PORT, db=settings.REDIS_DB)  # redis数据库连接信息
    def process_item(self, item, spider):
        if self.redis_db.exists(item['url']):
            raise DropItem('%s id exists!!' % (item['url']))
        else:
            self.redis_db.lpush(self.redis_table, item['url'])
        return item

class mysql_Pipeline(object):
    def open_spider(self,spider):
        self.mysql_db = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='root', db='mysql_test',charset='utf8')

    def close_spider(self,spider):
        self.mysql_db.close()

    def process_item(self,item,spider):
        try:
            sql=r"insert into runoob (title,text,create_time) values ('{}','{}','{}')".format(item['title'],item['text'],datetime.datetime.now())
            cursor=self.mysql_db.cursor()
            cursor.execute(sql)
            self.mysql_db.commit()
        except:
            print('%未抓取入库'%item['title'])