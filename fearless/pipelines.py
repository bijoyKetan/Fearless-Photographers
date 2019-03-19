# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from pymongo import MongoClient

# Inherit the  pipeline class
class FearlessPipeline(object):
    #Name of the collection where data will be stored
    collection = 'fearlessData'

    def __init__(self, mongo_uri, mongo_db):
        #uri => string used to identify a resource on network
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler (cls, crawler):
        return cls(
            mongo_uri = crawler.settings.get('MONGO_URI'),
            mongo_db = crawler.settings.get ('MONGO_DB')
        )

    # open the spier with connection
    def open_spider(self, spider):
        self.client= MongoClient(self.mongo_uri)
        self.db= self.client[self.mongo_db]
    
    #close the conection
    def close_spider(self):
        self.client.close()
    
    # process the data and insert into database
    def process_item(self, item, spider):
        self.db[self.collection].insert_one(dict(item))
        return item
