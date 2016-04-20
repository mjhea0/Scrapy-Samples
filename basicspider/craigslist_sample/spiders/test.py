from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from craigslist_sample.items import CraigslistSampleItem


class MySpider(BaseSpider):
    name = "craig"
    allowed_domains = ["craigslist.org"]
    start_urls = ["http://sfbay.craigslist.org/search/npo"]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        titles = hxs.xpath("//span[@class='pl']")
        items = []
        for title in titles:
            item = CraigslistSampleItem()
            item["title"] = title.select('a/span[@id="titletextonly"]/text()').extract()
            item["link"] = title.select("a/@href").extract()
            items.append(item)
        return items
