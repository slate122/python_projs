import scrapy

class detail_spider(scrapy.Spider):
    name = "detail"
    start_urls = ['https://books.toscrape.com/']

    def parse(self, response):
        book_url = response.css(".product_pod > h3 > a::attr(href)").getall()
        for book in book_url:
            yield response.follow(book,callback=self.parse_book)
        next_page = response.css('.next > a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
    
    def parse_book(self, response):
        price = response.css('.price_color::text').get()
        price = price.replace('£', '').strip() if price else price
        stock = response.css('.table > tr:nth-child(6) >td::text').get()
        stock = stock.replace('In stock (','').replace(' available)','').strip() if stock else stock
        stars = response.css('.product_main > p[class*=star]::attr(class)').get()
        stars = stars.replace('star-rating ','').strip() if stars else stars

        yield {
            "title": response.css('div.product_main > h1::text').get(),
            "price": price,
            "stock": stock,
            "cat": response.css('.breadcrumb >li:nth-child(3) > a::text').get(),
            "upc": response.css('.table > tr:nth-child(1) >td::text').get(),
            "type" : response.css('.table > tr:nth-child(2) >td::text').get(),
            "num_rev" : response.css('.table > tr:nth-child(7) >td::text').get(),
            "stars" : stars
        }

