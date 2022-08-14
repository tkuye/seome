# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SeometoolItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class PageLinkItem(scrapy.Item):
    """Scraped page link"""
    link = scrapy.Field()

class PageScriptItem(scrapy.Item):
    """Scraped injected javascript"""
    content = scrapy.Field()
