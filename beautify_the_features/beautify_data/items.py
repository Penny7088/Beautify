# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst


class BeautifyItem(scrapy.Item):
    # define the fields for your item here like:
    # NAME
    name = scrapy.Field()

    # 地址
    address = scrapy.Field()

    # 联系电话
    phone = scrapy.Field()

    # 公司
    company = scrapy.Field()
