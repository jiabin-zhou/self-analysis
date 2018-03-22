# -*- coding: utf-8 -*-
import scrapy
from scrapy_redis.spiders import RedisSpider
from ..items import NextUrlItem
from scrapy.selector import Selector

class DownloadTextSpider(RedisSpider):
    name = 'download_text'
    custom_settings = {'ITEM_PIPELINES': {'scrapy_redis_mysql.pipelines.mysql_Pipeline': 300, }}
    redis_key = 'need_urls'  # 从redis里面读url

    def parse(self, response):
        item=NextUrlItem()
        title=Selector(response=response).xpath(r'//div[@id="content"]/h1//text()').extract()
        text=Selector(response=response).xpath(r'//div[@id="content"]//text()').extract()
        #标题
        ti=''
        for i in title:
            ti+=i.replace('\r','').replace('\n','').replace('\t','').replace(' ','').replace('\\','').replace('/','')
        #把整张网页的教程以文本储存，但是储存在一个字段数据量太大，且可能有其它杂项字符，实际中不应用
        te=''
        for i in text:
            te+=i.replace('\r','').replace('\n','').replace('\t','').replace(' ','').replace('\\','').replace('/','')
        item['title']=ti
        item['text']=te
        yield item
