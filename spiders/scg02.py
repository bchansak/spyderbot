# -*- coding: utf-8 -*-
import scrapy
class SCG_Spider2(scrapy.Spider):
    name = "scg02"
    start_urls = [
        'https://www.scgshoppingexperience.com',
    ]

    def parse(self, response):
        for cat_url in response.css("div.product-dropdown > ul > li > a ::attr(href)").extract():
            yield scrapy.Request(response.urljoin(cat_url), callback=self.parse_cat_page)

    def parse_cat_page(self, response):
        for sub_cat_url in response.css("ul.category a.lvl2 ::attr(href)").extract():
            yield scrapy.Request(response.urljoin(sub_cat_url), callback=self.parse_sub_cat_page)

    def parse_sub_cat_page(self, response):
        for book_url in response.css("div.products a.product-link ::attr(href)").extract():
            yield scrapy.Request(response.urljoin(book_url), callback=self.parse_detail_page)
        next_page = response.css("div.fw-paginator-forward > div.fw-paginator-forward-txt > a ::attr(href)").extract_first()
        if next_page:
            yield scrapy.Request(response.urljoin(next_page), callback=self.parse_sub_cat_page)

    def parse_detail_page(self, response):
        item = {}
        item['product_status'] = ''.join(response.css('div.specification ::text').extract()).replace("\t", "")
        item['product_description'] = ''.join(response.css('div[role="textbox"]::text').extract()).replace("\t", "")
        item['product_price'] = response.css('div.price span::text').extract()
        item['product_name'] = response.css('div.product-name span::text').extract()
        item['product_id'] = response.css('div.product-id span::text').extract()
        yield item
    



