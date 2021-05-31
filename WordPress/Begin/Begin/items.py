# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BeginItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # title = scrapy.Field()
    link = scrapy.Field()


class BeginContent(scrapy.Item):
    title = scrapy.Field()
    content = scrapy.Field()
