import scrapy
from tutorial.items import TutorialItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.http.request.form import FormRequest
import json
import re

class DmozSpider(scrapy.Spider):
    name = 'dmoz'
    # allowed_domains = ['comic.kukudm.com']
    urls=[]
    for appid in ['xfm_yuanping04','guanglian05','guanglian07']:
        #url需要传递参数实现指定日期、渠道等的查询,为了安全...url部分做替换处理....
        urls.append('http://xxx.xx.xxx.xx:xxxx/statis/uv/retaining?searchDate=2018-01-01&num=15&appId=%s&channelId='%(appid))
    #重写start_requests
    def start_requests(self):
        #登陆，设置回调函数after_login
        return [scrapy.FormRequest('http://xxx.xx.xxx.xx:xxxx/login',
                                        formdata={'username':'用户名'},
                                        callback=self.after_login)]

    # def parse(self, response):
    #     return FormRequest.from_response(response,formdata={'username':'haizhong.chu@joyreach.com'},callback=self.after_login)

    def after_login(self,response):
        print(response.body.decode('utf-8'))
        for url in self.urls:
            #登陆后向构造好的url发送request请求，设置回调函数liucun
            yield scrapy.Request(url,callback=self.liucun)

    def liucun(self,response):
        item=TutorialItem()
        need=json.loads(response.body)
        result=need['result']
        for i in range(len(result)):
            item['date']=result[i]['date']
            item['count']=result[i]['count']
            item['rate']=result[i]['rate']
            item['appid']=re.search('appId=(\S+)&',response.url).group(1)
            yield item