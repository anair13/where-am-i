# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class LandmarksItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    country = scrapy.Field()
    region = scrapy.Field()
    coordinates = scrapy.Field()
    latitide = scrapy.Field()
    longitude = scrapy.Field()
    caption = scrapy.Field()
    url = scrapy.Field()