#Import the spiders and items
from fearless.items import FearlessItem
from fearless.spiders.fearless_scrp import FearlessScraper
from fearless.spiders.inquiryReply import ReplySpider

#Import the required packages and modules for scraping
import scrapy
from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings


configure_logging()
runner = CrawlerRunner(settings=get_project_settings())

@defer.inlineCallbacks
def crawl():
    yield runner.crawl(FearlessScraper)
    yield runner.crawl(ReplySpider)
    reactor.stop()

crawl()
reactor.run() # the script will block here until the last crawl call is finished