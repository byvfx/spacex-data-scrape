import scrapy
import json


class SpacexSpySpider(scrapy.Spider):
    name = 'spacex_spy'
    allowed_domains = ['spacexdata.com']
    start_urls = ['https://api.spacexdata.com/v4/launches']

    def parse(self, response):
        data = json.loads(response.body)
        for launch in data:
            yield {
                'flight_number': launch.get('flight_number'),
                'mission_name': launch.get('name'),
            
            }
