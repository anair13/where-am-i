# -*- coding: utf-8 -*-
import scrapy
from scrapy.shell import inspect_response
from landmarks.items import LandmarksItem

class LandmarksSpider(scrapy.Spider):
    name = "Landmarks"
    allowed_domains = ["whc.unesco.org"]
    start_urls = ["http://whc.unesco.org/en/list/" + str(i) for i in range(1, 1419)]

    def parse(self, response):
        infobox = response.xpath('//*[@id="sidebar"]/div/div[1]/div')
        if infobox:
            data = [s.strip() for s in infobox.xpath('div//text()').extract()]
            i = LandmarksItem()
            i['name'] = response.xpath('//*[@id="content"]/div/div/h1/text()').extract()[0]
            i['caption'] = response.xpath('//*[@id="contentdes_en"]/p/text()').extract()[0]
            i['country'] = data[2]
            i['region'] = data[4]
            i['url'] = response.url
            i['coordinates'] = data[6]
            yield i