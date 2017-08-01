import scrapy
class QuotesSpider(scrapy.Spider):
    name = "scg01"
    start_urls = [
        'https://www.scgshoppingexperience.com/scgmain/catalog/productDetail.xhtml?area=1100010100&sort=ID&wec-appid=SCGMAIN&page=DCD3B84092B6493CBFEB5966F2CC79C4&itemKey=001018A5ACDE1EE2BE8A1B3AE0C45888&show=12&view=grid&wec-locale=th'
    ]

    def parse(self, response):
        yield {
                'productId': response.css('div.product-id span::text').extract(),
                'product-name': response.css('div.product-name span::text').extract(),
                'description': response.css('div[role="textbox"]::text').extract(),
                'product_status' : ''.join(response.css('div.specification ::text').extract()).replace("\t", ""),
            }
        # count = 1
        # for quote in response.css('div.detail-info').extract():
        #     print count
        #     count = count+1
            

        # for quote2 in response.css('div.detail-info').extract():
        #     print count
        #     count = count+1
        #     yield {
        #         'description': response.css('div[role="textbox"]::text').extract(),
        #     }