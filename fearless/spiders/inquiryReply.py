import scrapy
from scrapy.http import FormRequest
import logging
from fearless.items import FearlessItem
from pymongo import MongoClient
import datetime
from pytz import timezone
from fearless import settings, pipelines


class ReplySpider(scrapy.Spider):
    # #Testing by connecting to local database
    # client = MongoClient('mongodb://127.0.0.1:27017')
    # db = client.fearless

    # Connect to Heroku database
    client = MongoClient(settings.MONGO_URI,
                     connectTimeoutMS=30000,
                     socketTimeoutMS=None,
                     socketKeepAlive=True)
    db = client.get_default_database()
    
    #Photographer for whom the replied will be made.
    photographer_id = '5138'

    #Spider identity
    name = 'inquiryReply'

    #Allowed domains
    allowed_domains = ['fearlessphotographers.com']

    #Current time (EST)
    tz = timezone ('EST')
    currentTime = str(datetime.datetime.now(tz))

    # The start URLs are filters to contain only those RequestLink that:
    # 1. Do not have the field "Replied"
    # 2. Country = { USA, Mexico, Canada}
    start_urls = db.fearlessData.distinct ('RequestLink', {'$and':[
        {'Country': {'$in': ["USA", "Canada",  "Mexico"]}},
        { "Replied": {'$exists': False}}]})
    
    def parse(self, response):
        
        #Query that inserts a new field in the document, Replied60, and sets it to True.
        self.db.fearlessData.update_many({'RequestLink': response.url},{'$set':{"Replied":True}})

        #Insert a new field with the timestamp when reply is sent
        self.db.fearlessData.update_many({'RequestLink': response.url},{'$set':{"RepliedTime":self.currentTime}})

        #Make the POST request to filtered inquiries.
        yield scrapy.FormRequest.from_response (response, formdata = {
                'submitresponse': '1',
                'secretNumberHash': response.xpath("//input[@name = 'secretNumberHash']/@value").get(),
                'photogID': self.photographer_id,
                'secretNumber': response.xpath("//b[@style = 'color:#e79545;']/text()").get(),
                'subject': ''
            }, callback=self.after_login)
            
        
    def after_login(self, response):
        logging.info(response.status)
