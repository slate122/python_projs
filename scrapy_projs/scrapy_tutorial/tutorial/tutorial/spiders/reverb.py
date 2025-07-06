import scrapy

class reverb_spider(scrapy.Spider):
    name = "reverb"
    start_urls = ['https://www.chicagomusicexchange.com/collections/electric-guitars']

    def parse(self, response):
        for guitar in response.css('ul.product-grid > li'):
            yield {
                "listing": guitar.css('div.product-cars__image > img::attr(title)').get(),
                "price": guitar.css('span.visually-hidden::text').get(),
                "condition": guitar.css('div.rc-listing-card__condition::text').get()
            }
        #next_page = response.css('a.pagination_button::attr(href)').get()
        #if next_page is not None:
            #yield response.follow(next_page, callback=self.parse)
    
