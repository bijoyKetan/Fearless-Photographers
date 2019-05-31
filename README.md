# Extract and Analyze Wedding Data & Respond to Client Inquiries Systematically

#### Overview:
[Fearless Photographers](https://www.fearlessphotographers.com/find-wedding-photographers.cfm)  is a wedding photography website where potential bride/grooms can inquire about photographers to cover their weddings. Similary, interested and available photographers can mark themselves available to be considered by the couple. The couple can suqsequently review the portfolio of photographers who expressed interest and initiate possible booking process/follow up discussions accordingly. In essense, the website provides a marketplace to connect buyers and sellers of wedding photography service. 

The core objectives of this exercise are the follwoing:
1. Implement a webscraping application that extracts inquiry information from fearless website.
2. Aggregate, process, analyze and draw insighst based on the data that have been scraped from fearlessphotographers.com 
3. Implement a mechanism to respond to wedding photography inquiries based on a set of predefined criteria (e.g. location, date etc.)
4. Deploy the application to a PaaS (Platform as a Service) provider so that scheduled jobs can be run to perform the scraping and responding tasks automatically at predefibned intervals. 

#### Summary of key steps for implementation:
1. Scrape wedding inquiry information using Scrapy spider and XPath selectors.
2. Store the scraped data in a non-relational (MongoDB) database.
3. Scraped information include the following:
    - Client ID
    - Event date
    - Event location
    - Type of event
    - Number of photographers who already replied
    - Time of scrape
4. Implement a second spider that replies to cleint inquiries (on behanf of a given photographer) based on a set of predefined rules (e.g. reply if the weddins is in USA, Mexico or Canada).
5. When spider 2 replies to an inquiry, it also records the time of that response and inserts a new field into that collection, Replied (boolean). 
6. Write a script that runs the two spiders periodically.The Replied field in spider 2helps filter out inquirues that have already been replied to, eliminating the possibility of spider 2's replying to an ever increasing number of inquiries in each run. 
7. Deploy the project to a PasS provider (Heroku).
    
    
---
