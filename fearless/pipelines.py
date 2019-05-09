# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from pymongo import MongoClient
from scrapy.exceptions import DropItem

# Inherit the  pipeline class
class MongoDbPipeline(object):
    #Name of the collection where data will be stored
    collection = 'fearlessData'

    def __init__(self, mongo_uri, mongo_db):
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

    # process the data and insert into database
    # The DropItem exception avoids dplicate enntries in database
    def process_item(self, item, spider):
        if self.db[self.collection].count_documents({'ID': item.get("ID")}) == 1:
            raise DropItem ("Item dropped to avoid duplicate insert")
        else:
            self.db[self.collection].insert_one(dict(item))
            return item  

    #close the conection
    def close_spider(self):
        self.client.close()
    

