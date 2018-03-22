# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import Spider
from ..items import MainUrlItem
from scrapy.selector import Selector


class RunoobSpiderSpider(Spider):
    name = 'runoob_spider'
    custom_settings = {'ITEM_PIPELINES':{'scrapy_redis_mysql.pipelines.redis_Pipeline': 300,}}
    allowed_domains = ['runoob.com']
    start_urls = ['http://www.runoob.com/']

    def parse(self,response):
        first_url=Selector(response=response).xpath(r'//div[@class="col middle-column-home"]/div[contains(@class,"codelist codelist-desktop cate")]/a/@href').extract()
        for firsturl in first_url:
            yield scrapy.Request('http://'+firsturl[2:],callback=self.set_url)

    def set_url(self,response):
        item=MainUrlItem()
        main_url=Selector(response=response).xpath(r'//div[@id="leftcolumn"]/a/@href').extract()
        for url in main_url:
            if url[:7]=='http://':
                item['url'] = url
            else:
                item['url']='http://www.runoob.com'+url
            yield item