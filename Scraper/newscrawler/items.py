# -*- coding: utf-8 -*-
import scrapy

class NewsItem(scrapy.Item):
	url = scrapy.Field()
	headline = scrapy.Field()
	author = scrapy.Field()
	content = scrapy.Field()
	tags = scrapy.Field()