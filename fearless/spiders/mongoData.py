
#**********************************************
#Note: This is a test file only. Not part of the project.
#Created to test pymongo queries to access and update 
#data in the noSQL database
#**********************************************


# from pymongo import MongoClient
# from pprint import pprint

# #Connent to mongoDB client and to the database
# client = MongoClient('mongodb://127.0.0.1:27017')
# db = client.fearless

#**********************************************
#Comment/uncomment the following sections to test these snippets of code.
#**********************************************

 
#**********************************************

# links2 = db.fearlessData.distinct ('Name', 
#     {'$and':[
#     # {'Country': {'$in': ["USA", "Canada",  "Mexico"]}},
#     {'Country': {'$in': ["South Africa"]}},
#     {"Replied":""}]}
#     )
# pprint (links2)

# countryCount = db.fearlessData.find(
# #    {'Country': {'$in': ["Anjali", " Canada", " Mexico"]}}
#    {}
# ).count()
# print (countryCount)

# db.fearlessData.update_many ({},{'$set': {'Replied': ""}})

#**********************************************




#**********************************************

# data_set_1 = db.fearlessData.find(
#  {"Replied": {"$exists": False}},
#  {"_id":1, "RequestLink":1}   
# )

# requestList = []
# idList = []
# for myDict in data_set_1:
#     try:
#         requestList.append(myDict['RequestLink'])
#         idList.append(myDict['_id'])

#     except:
#         pass

# print (requestList[0])
# print (idList[0])
#**********************************************



#**********************************************
# Insert a new field, Replied, and set it to True when post request is made 
# db.fearlessData.update_many({},{'$set':{"New_Field":"TEST_Wedding_v5"}})
# db.fearlessData.update_many({},{'$set':{"Replied":"Ketan"}})

# db.fearlessData.update_one({},{'$set':{"Replied3":"YOLO"}})
# print (db.fearlessData.find({}))

# Find list of all URLs
# links = db.fearlessData.find(
#     {},{'RequestLink':1,"_id":0,'Name':1 }
# )
#**********************************************



# requestFormID = response.xpath("//div[@class='navbar']/following-sibling::text()").get().strip().replace("Request", "").replace("#","").strip() 
# locations = ["ny - usa", "nj - usa"]
# location = response.xpath("//span[@class = 'info-label' and contains(text(),'Location')]/following-sibling::text()[1]").get().lower().split(",")[-1].strip()