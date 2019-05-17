import scrapy
import logging


class AllinquiriesSpider(scrapy.Spider):
    '''
    Creating a scraper to scrape all the old (not available on inquiry page) inquiry data. 
    '''
    name = 'allInquiries'

    # We're going to crawl only 250 pages per scraping seesion.
    # This is to ensure we scrape the website gently.   
    # For this website, we'll scrape from ID 1000 - 8000  
    start_request = 6000
    end_request = start_request+249

    def start_requests(self):
        yield scrapy.Request(url="https://www.fearlessphotographers.com/find-wedding-photographers.cfm?requestID={}".format(self.start_request),
        meta={
            'dont_redirect': True,
            'handle_httpstatus_list': [302]
        })
    
    requestId = start_request
    def parse(self, response):
        # logging.info(response.request.headers)
        # The redirected page for missing pages has the h1 header text, "Find your photographer fast!"
        not_found = response.xpath("//div[@class='title-bg']/h1/text()").get()
        if not_found != 'Find your photographer fast!':
            yield{
                "ID": response.url.split("=")[-1],
                "Name": response.xpath("//div[@class='content']/div[@class='col bodytext']/span[@class='info-label' and contains(text(), 'Name:')]/following::text()[1]").get(),
                "Date": response.xpath("//div[@class = 'col bodytext']/child::text()[4]").get(),
                "Location": response.xpath("//div[@class = 'col bodytext']/child::text()[6]").get(),
                "Type": response.xpath("//div[@class = 'col bodytext']/child::text()[8]").get(),
                "Replies": response.xpath("//div[@class='subtitle']/text()").getall(),
                "RequestLink": response.url
            }

            if self.requestId <= self.end_request:
                self.requestId += 1
                new_url = 'https://www.fearlessphotographers.com/find-wedding-photographers.cfm?requestID={}'.format(self.requestId)  
                yield scrapy.Request(url=new_url, callback=self.parse, meta= {
                    'dont_redirect': True,
                    'handle_httpstatus_list': [302]
                }, dont_filter=True)