from pymongo import MongoClient
from pprint import pprint
import datetime
import pytz

client = MongoClient('mongodb://127.0.0.1:27017')
db = client.fearless

# Print all RequestLinks where Country in (Canada, USA)
start_urls = db.fearlessData.distinct('RequestLink',
                                      {'$and': [
                                          {'Country': {
                                           '$in': ["Canada", "USA"]}}
                                      ]})
pprint(start_urls)

# Get current EST time
tz = pytz.timezone('EST')
pprint(str(datetime.datetime.now(tz)))

# Print all the wedding dates in an array
print(db.fearlessData.find({}, {'Name': 1, '_id': 0}))


# Test Logic
test_urls = db.fearlessData.distinct('RequestLink', {'$and': [
    {'Country': {'$in': ["Romania"]}},
    {"Replied": {'$exists': False}}]})

pprint (test_urls)


# print ((pytz.utc))
# print (pytz.timezone('US/Eastern'))