import scrapy
from scrapy.http import FormRequest
import logging
from fearless.items import FearlessItem
from pymongo import MongoClient


class ReplySpider(scrapy.Spider):
    #Connent to mongoDB client and to the database
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.fearless
    
    #Photographer for whom the replied will be made.
    photographer_id = '5138'

    #Spider identity
    name = 'inquiryReply'

    allowed_domains = ['fearlessphotographers.com']

    # The start URLs are filters to contain only those RequestLink that:
    # 1. Do not have the field "Replied"
    # 2. Country = { USA, Mexico, Canada}
    start_urls = db.fearlessData.distinct ('RequestLink', {'$and':[
        {'Country': {'$in': ["USA", "Canada",  "Mexico"]}},
        { "Replied": {'$exists': False}}]})
    
    def parse(self, response):
        
        #Query that inserts a new field in the document, Replied60, and sets it to True.
        self.db.fearlessData.update_many({'RequestLink': response.url},{'$set':{"Replied":True}})

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
