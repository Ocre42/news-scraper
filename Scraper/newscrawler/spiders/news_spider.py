# -*- coding: utf-8 -*-
import scrapy

class NewsSpider(scrapy.Spider):
    name = "news"
    start_urls = ["http://www.bbc.com/news"]

    def parse(self, response):
        for href in response.css('div a.gs-c-promo-heading::attr(href)'):
            yield response.follow(href, self.parse_item)
        for link in response.css('li.gs-o-list-ui__item--flush a.nw-o-link::attr(href)'):
            if link != '/news/video_and_audio/headlines':
                yield response.follow(link, self.parse_link)

    def parse_link(self,response):
        for href in response.css('a.title-link::attr(href)'):
            yield response.follow(href, self.parse_item)

    def parse_item(self, response):
        if response.css('h1.story-body__h1::text').extract_first() or response.css('span.cta::text').extract_first():
            if response.css('h1.story-body__h1::text').extract_first():
                title = response.css('h1.story-body__h1::text').extract_first()
            else:
                title = response.css('span.cta::text').extract_first()
            if response.css('nav.navigation-wide-list a.secondary-navigation__title span::text').extract_first():
                cat = response.css('nav.navigation-wide-list a.secondary-navigation__title span::text').extract_first()
            elif response.css('span.index-title__container a::text').extract_first():
                cat = response.css('span.index-title__container a::text').extract_first()
            else:
                cat = response.css('ul.navigation-wide-list li.selected a span::text').extract_first()        

            yield{
                'Title': title,
                'Tags': response.css('ul.tags-list li a::text').extract(),
                'Category': cat,
                'Content': response.css('div.story-body__inner p::text').extract()
            }