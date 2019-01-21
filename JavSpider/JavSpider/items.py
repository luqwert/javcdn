# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JavspiderItem(scrapy.Item):
    # define the fields for your item here like:
    number = scrapy.Field()
    title = scrapy.Field()
    pdate = scrapy.Field()
    detail_link = scrapy.Field()
    cover = scrapy.Field()
    fenlei = scrapy.Field()
    actor = scrapy.Field()
    maglinks = scrapy.Field()

