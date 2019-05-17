import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst
from scrapy import Request
from urllib.parse import urljoin

def cleanID(rawID):
    return rawID.replace("#","")

#Extract the city from location string, e.g. 'Kliplapa - South Africa'
def getCity(location):
    return location.split('-')[0]

#Extract the city from location string, e.g. 'Kliplapa - South Africa'
def getCountry (location):
    return location.split('-')[-1]

def finalUrl (relativeurl):
    return urljoin(base = 'https://www.fearlessphotographers.com/find-wedding-photographers.cfm', url = relativeurl)

def remove_Spaces(rawString):
    return rawString.strip()

class FearlessItem(scrapy.Item):

    ID = scrapy.Field(
        input_processor = MapCompose(cleanID),
        output_processor = TakeFirst()
    )

    Name = scrapy.Field(
        input_processor = MapCompose(remove_Spaces),
        output_processor = TakeFirst()
    )  
    Date =  scrapy.Field(
        input_processor = MapCompose(remove_Spaces),
        output_processor = TakeFirst()
    )

    City= scrapy.Field(
        input_processor = MapCompose (getCity),
        output_processor = TakeFirst()
    )
    Country= scrapy.Field(
        input_processor = MapCompose (getCountry, remove_Spaces),
        output_processor = TakeFirst()
    )
    Type=  scrapy.Field(
        input_processor = MapCompose(remove_Spaces),
        output_processor = TakeFirst()
    )

    Available= scrapy.Field(
        input_processor = MapCompose(remove_Spaces),
        output_processor = TakeFirst()
    )

    RequestLink = scrapy.Field(
        input_processor = MapCompose(finalUrl),
        output_processor = TakeFirst()
    )

    Replied = scrapy.Field(
        output_processor = TakeFirst()
    )

    ScrapedTime = scrapy.Field(
        output_processor = TakeFirst()
    )