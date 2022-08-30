import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class AmazondealsSpider(CrawlSpider):
    name = 'AmazonDeals'
    allowed_domains = ['amazon.in']
    start_urls = ['https://www.amazon.in/s?k=mobile+phones&page=2&crid=37TS853BIU4O2&qid=1661850924&sprefix=mobile+phones%2Caps%2C225&ref=sr_pg_1']

    rules = (
        Rule(LinkExtractor(restrict_xpaths=("//h2[@class='a-size-mini a-spacing-none a-color-base s-line-clamp-2']/a")), callback='parse_item', follow=True),
        # Rule(LinkExtractor(restrict_xpaths="//a[@class='s-pagination-item s-pagination-next s-pagination-button s-pagination-separator']")),
    )

    def parse_item(self, response):
        
        item = {}
        item['product_name'] = response.xpath('normalize-space(//h1[@class="a-size-large a-spacing-none" or @class="a-size-large a-spacing-none"]/span/text())').get()
        item['price'] = response.xpath("//span[@class='a-price a-text-price a-size-medium apexPriceToPay' or @class='a-price aok-align-center reinventPricePriceToPayMargin priceToPay']//span[1]/text()").get()
        item['description'] = response.xpath("//ul[@class='a-unordered-list a-vertical a-spacing-mini']//span/text()").get()
        item['Urls']=response.url
        return item
        
