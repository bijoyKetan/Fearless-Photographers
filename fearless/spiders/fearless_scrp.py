import scrapy
from scrapy.loader import ItemLoader
from fearless.items import FearlessItem
from fearless.spiders.inquiryReply import ReplySpider
from scrapy.crawler import CrawlerProcess

from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging


#First spider that scrapes the inquiries from potential clients. 
class FearlessScraper (scrapy.Spider):
    #identity
    name = "fearless"
    
    #Request
    def start_requests(self):
        start_url= 'https://www.fearlessphotographers.com/find-wedding-photographers.cfm'
        yield scrapy.Request (url=start_url, callback = self.parse)
        

    #Response
    def parse(self, response):

        for inquiry in response.xpath("//div[@id = 'requestlisting']/a"):
            loader = ItemLoader (item = FearlessItem(), selector=inquiry, response = response)
            loader.add_xpath(field_name = 'ID', xpath = ".//div[@class = 'title']/text()[1]")
            loader.add_xpath(field_name = 'Name', xpath = ".//span[@class='info-label' and position() = 1]/following-sibling::text()[1]")
            loader.add_xpath(field_name = 'Date', xpath = ".//span[@class='info-label' and position() = 2]/following-sibling::text()[1]")
            loader.add_xpath(field_name = 'City', xpath = ".//span[@style ='color:#e79545;']/text()")
            loader.add_xpath(field_name = 'Country', xpath = ".//span[@style ='color:#e79545;']/text()")
            loader.add_xpath(field_name = 'Type', xpath = ".//span[@class='info-label' and position() = 5]/following-sibling::text()[1]")
            loader.add_xpath(field_name = 'Available', xpath = ".//span[@class='info-label' and position() = 6]/following-sibling::text()[1]")
            loader.add_xpath(field_name = 'RequestLink', xpath = ".//@href")
            loader.add_value(field_name = 'Replied', value='')
            yield loader.load_item()
