import scrapy
from scrapy import Selector

class ShopcluespiderSpider(scrapy.Spider):
    name = "shopclueSpider"
    allowed_domains = ["shopclues.com"]
    start_urls = ["https://www.shopclues.com/mobiles-and-tablets.html?page=1"]

    def parse(self, response):
        # Extract the products
        products = response.css(".column.col3").getall()

        products_links = []
        for product in products:
            product_selector = Selector(text=product)
            link = product_selector.css("a[href^='//']::attr(href)").get()
            if link:
                products_links.append(f"https:{link}" if link.startswith("//") else link)

        # Print the total number of product links found
        self.logger.info(f"Total Products links: {len(products_links)}")

        # Follow each product link to extract details
        for link in products_links:
            yield scrapy.Request(url=link, callback=self.parse_product_details)

        # Get the current page number
        current_page = int(response.url.split('=')[-1])

        # Check if there's a next page
        if products[-1]:
            next_page = current_page + 1
            next_page_url = f"https://www.shopclues.com/mobiles-and-tablets.html?page={next_page}"
            self.logger.info(f"Scraping next page: {next_page_url}")
            yield response.follow(next_page_url, callback=self.parse)

    def parse_product_details(self, response):
        # Extract the product details
        name = response.css("h1::text").get()
        brand = response.css("span.pID a::text").get()
        ratingCount = response.css("span.rating_num::text").get()
        total_reviews = response.css("a#scrolltoreview::text").get()
        ratingValue = response.css('span[itemprop="ratingValue"]::text').get()
        price = response.css('span.f_price::text').get()
        seller_name = response.css('div[itemprop="seller"] h3[itemprop="name"]::text').get()
        seller_location = response.css('div[itemprop="seller"] p::text').get()
        seller_store_link = response.css('div[itemprop="seller"] a::attr(href)').get()
        
        # Clean and log extracted data
        product_details = {
            "name": name.strip() if name else None,
            "brand": brand.strip() if brand else None,
            "rating_count": ratingCount.replace("(", "").replace(")", "") if ratingCount else 0,
            "total_reviews": total_reviews.replace("(", "").replace(")", "") if total_reviews else 0,
            "rating_value": ratingValue if ratingValue else 0,
            "price": price.replace("₹", "") if price else None,
            "seller_name": seller_name.strip() if seller_name else None,
            "seller_location": seller_location.strip() if seller_location else None,
            "seller_store_link": seller_store_link
        }
        self.logger.info(f"Product Details: {product_details}")

        yield product_details
