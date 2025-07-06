import scrapy

class bookspider(scrapy.Spider):
    name = "books"
    start_urls = ['http://books.toscrape.com/index.html']
    
    def parse(self, response):
        for c in response.css(".nav > li:nth-child(1) > ul:nth-child(2) > li > a"):
            next_url = c.attrib['href']  # or c.css('::attr(href)').get()
            category_name = c.css('::text').get().strip()
            yield response.follow(next_url, callback = self.parse_category, meta={"category": category_name})



    def parse_category(self, response):
        category_name = response.meta.get("category")
        for book in response.css("article.product_pod"):
            title = book.css('h3 > a::attr(title)').get()
            price = book.css('p.price_color::text').get()
            instock = ''.join(book.css('p.instock.availability::text').getall()).strip()
            rating = book.css('p::attr(class)').get()
            clean_price = price.replace('£', '').strip() if price else price
            yield {"Title": title, "Price" : clean_price, "Rating":rating,"Category" : category_name, "Instock": instock}
        next_page = response.css("li.next > a::attr(href)").get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse_category, meta={"category": category_name})