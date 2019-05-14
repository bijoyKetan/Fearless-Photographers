from pymongo import MongoClient
from pprint import pprint

client = MongoClient('mongodb://127.0.0.1:27017')
db = client.fearless

start_urls = db.fearlessData.distinct ('RequestLink', 
    {'$and':[
    {'Country': {'$in': ["Canada", "USA"]}}
    ]})

pprint(start_urls)