# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BaiducrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    url = scrapy.Field()
    app_id = scrapy.Field()
    Author = scrapy.Field()
    category = scrapy.Field()
    score = scrapy.Field()
    reviews = scrapy.Field()
    Updated = scrapy.Field()
    Size = scrapy.Field()
    installs = scrapy.Field()
    CurrentVersion = scrapy.Field()
    RequiresAndroid = scrapy.Field()
    ContentRating = scrapy.Field()
    developer_email = scrapy.Field()
    
    ymllist=scrapy.Field()
    content = scrapy.Field()
    yml=scrapy.Field()
    list1=scrapy.Field()

    







