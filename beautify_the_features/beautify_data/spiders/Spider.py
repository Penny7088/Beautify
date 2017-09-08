# -*- coding: utf-8 -*-
from scrapy_redis.spiders import RedisSpider
from scrapy.http import Request

from scrapy.spiders import CrawlSpider
from beautify_data.items import BeautifyItem
import urllib
import sys
import string

reload(sys)
sys.setdefaultencoding('utf-8')

'''
美团app 美容相关的数据
'''
class beautify_data(RedisSpider):
    name = 'beautify_data'
    redis_key = 'beautify_data:start_urls'
    start_urls = ['http://i.meituan.com/wuhan?cid=22']
    page_num = 63
    child_head = 'http://i.meituan.com/wuhan?cid=22&p='
    detail_head = 'http://'
    #lpush beautify_data:start_urls http://i.meituan.com/wuhan?cid=22

    def parse(self, response):
        print "haha:" + response.url

        for i in range(1, self.page_num):
            s = str(i)
            url = self.child_head + s
            print "=====:" + url
            yield Request(url=url, callback=self.parse_child, dont_filter=True)

    def parse_child(self, response):
        url_list = response.xpath(
            './/*[@id="deals"]/dl/dd[1]/a/@href').extract()
        for url in url_list:
            split_url = url.split('//')
            page_url = self.detail_head + split_url[1]
            yield Request(url=page_url, callback=self.parse_detail, dont_filter=True)

    def parse_detail(self, response):
        item = BeautifyItem()

        item["address"] = response.xpath('.//*[@id="deal-list"]/dl[1]/dd/dl/dd[2]/div/h6/a/div/text()').extract_first()
        item["phone"] = response.xpath(
            './/*[@id="deal-list"]/dl[1]/dd/dl/dd[2]/div/p/a/@data-tele').extract_first()
        item["company"] = response.xpath(
            './/*[@id="deal-list"]/dl[1]/dd/dl/dd[1]/div/h1/text()').extract_first()
        yield item
