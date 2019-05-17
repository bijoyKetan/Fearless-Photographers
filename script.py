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

#Import packages for schedling spiders
import requests, pytz
from apscheduler.schedulers.twisted import TwistedScheduler

#Execute the spiders every X hours

configure_logging()
runner = CrawlerRunner(settings=get_project_settings())

@defer.inlineCallbacks
def crawl():
    yield runner.crawl(FearlessScraper)
    yield runner.crawl(ReplySpider)
    reactor.stop()



if __name__ == '__main__':
    scheduler = TwistedScheduler(timezone = pytz.timezone('US/Eastern'))
    scheduler.add_job (crawl,'cron', day_of_week = 'mon-sun', hour = '16', minute = '0')
    schedueler.start()

    # crawl()
    reactor.run()