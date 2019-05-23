# Import the spiders and items
from fearless.items import FearlessItem
from fearless.spiders.fearless_scrp import FearlessScraper
from fearless.spiders.inquiryReply import ReplySpider

# Import the required packages and modules for scraping
import scrapy
from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings
import os 
from scrapy.crawler import CrawlerProcess

# Import packages for schedling spiders
import requests
import pytz
from apscheduler.schedulers.twisted import TwistedScheduler
from apscheduler.schedulers.blocking import BlockingScheduler

# Execute the spiders every X hours

configure_logging()
# runner = CrawlerRunner(settings=get_project_settings())


# @defer.inlineCallbacks
# def crawl_spider_1():
#     yield runner.crawl(FearlessScraper)
#     #reactor.stop()


# @defer.inlineCallbacks
# def crawl_spider_2():
#     yield runner.crawl(ReplySpider)
#     reactor.stop()

def runSpider ():
    process = CrawlerProcess(settings=get_project_settings())
    process.crawl(FearlessScraper)
    process.crawl(ReplySpider)
    process.start() # the script will block here until all crawling jobs are finished




if __name__ == '__main__':
    scheduler = BlockingScheduler(timezone=pytz.timezone('US/Eastern'))
    scheduler.add_job(runSpider, 'cron', day_of_week='mon-sun',
                      hour='18', minute='22')
    
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    # Execution will block here until Ctrl+C (Ctrl+Break on Windows) is pressed.
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass

    scheduler.start()

#     # crawl()