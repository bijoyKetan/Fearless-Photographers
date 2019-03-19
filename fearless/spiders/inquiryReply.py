import scrapy
from scrapy.http import FormRequest
import logging
 
 
class MyspiderSpider(scrapy.Spider):
    name = 'inquiryReply'
    allowed_domains = ['fearlessphotographers.com']
    start_urls = ['https://www.fearlessphotographers.com/find-wedding-photographers.cfm?requestID=8434']
    

    def parse(self, response):
        
        photographerID = '5138'
        requestFormID = response.xpath("//div[@class='navbar']/following-sibling::text()").get().strip().replace("Request", "").replace("#","").strip() 
        locations = ["ny - usa", "nj - usa"]
        location = response.xpath("//span[@class = 'info-label' and contains(text(),'Location')]/following-sibling::text()[1]").get().lower().split(",")[-1].strip()
        
        if location in locations: 
            yield scrapy.FormRequest.from_response (response, formdata = {
                    'submitresponse': '1',
                    'requestID': requestFormID,
                    'secretNumberHash': response.xpath("//input[@name = 'secretNumberHash']/@value").get(),
                    'photogID': photographerID,
                    'secretNumber': response.xpath("//b[@style = 'color:#e79545;']/text()").get(),
                    'subject': ''
                }, callback=self.after_login)
        
    def after_login(self, response):
        logging.info(response.status)
