import scrapy

class AllinquiriesSpider(scrapy.Spider):
    '''
    Creating a class to sscrape all the old (not available on inquiry page) inquiry data. 
    '''
    name = 'allInquiries'
    allowed_domains = ['fearlessphotographers.com']
    
    #Request
    def start_requests(self):    
        for x in list (range(1000, 1005)):
            start_url= 'https://www.fearlessphotographers.com/find-wedding-photographers.cfm?requestID={}'.format(x)           
            yield scrapy.Request (url=start_url, callback = self.parse)

    
    def parse(self, response):

        yield{

            "ID": response.url.split("=")[-1],
            "Name": response.xpath("//div[@class = 'col bodytext']/child::text()[2]").get().strip(),
            "Date": response.xpath("//div[@class = 'col bodytext']/child::text()[4]").get().strip(),
            "City": response.xpath("//div[@class = 'col bodytext']/child::text()[6]").get().split('-')[0].strip(),
            "Country": response.xpath("//div[@class = 'col bodytext']/child::text()[6]").get().split('-')[-1].strip(),
            "Location": response.xpath("//div[@class = 'col bodytext']/child::text()[6]").get().strip(),
            "Available": int (response.xpath("//div[@class='subtitle']/text()[1]").get()[0]) + int (response.xpath("//div[@class='subtitle']/text()").getall()[1][0]), 
            "RequestLink": response.url
        }