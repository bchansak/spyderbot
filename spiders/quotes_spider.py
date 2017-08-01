import scrapy
class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'https://www.scgshoppingexperience.com/scgmain/catalog/productDetail.xhtml?area=1300010100&sort=ID&wec-appid=SCGMAIN&page=DCD3B84092B6493CBFEB5966F2CC79C4&itemKey=001018A5ACDE1EE2BE8A1A0F9C231888&show=12&view=grid&wec-locale=th'
    ]

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)