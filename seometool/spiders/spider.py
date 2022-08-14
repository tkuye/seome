import sys
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from urllib.parse import urlparse
from scrapy.crawler import CrawlerProcess
import scrapy
from seometool.items import PageLinkItem, PageScriptItem
from scrapy_splash import SplashRequest
    
class SiteSpider(scrapy.Spider):
    name = "sitespider"
    def __init__(self, url=None, *args, **kwargs):
        super(SiteSpider, self).__init__(*args, **kwargs)
        
        if url is None:
            print("Please provide a start url")
            sys.exit(1)
        
        self.start_urls = [url]
        domain = urlparse(self.start_urls[0]).netloc
        self.allowed_domains = [domain]
        
    async def parse(self, response):
        page = response.meta["playwright_page"]
 
        for link in self.get_links(response):
            yield link
        
        for script in self.get_scripts(response):
            yield script
        
        await page.close()

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url,
                self.parse, 
                 meta={"playwright": True, "playwright_include_page": True},)

    def get_scripts(self, response):
        scripts = response.xpath('//html//script').extract()
        for script in scripts:
            item = PageScriptItem()
            item['content'] = script
            yield item

    def get_links(self, response):
        links = response.xpath('//a/@href').extract()
        for link in links:
            item = PageLinkItem()
            item['link'] = link
            yield item
    
            

