from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from craigslist_sample.items import CraigslistSampleItem

class MySpider(CrawlSpider):
	name = "craigs"
	allowed_domains = ["craigslist.org"]
	start_urls = ["http://sfbay.craigslist.org/npo/"]
	
	rules = (Rule (SgmlLinkExtractor(allow=("index\d00\.html", ),restrict_xpaths=('//p[@id="nextpage"]',))
	, callback="parse_items", follow= True),
	)	

	def parse_items(self, response):
		hxs = HtmlXPathSelector(response)
		titles = hxs.select("//p")
		items = []
		for titles in titles:
			item = CraigslistSampleItem()
			item ["title"] = titles.select("a/text()").extract()
			item ["link"] = titles.select("a/@href").extract()
			items.append(item)
		return items		
