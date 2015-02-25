# Define here the models for your scraped items

from scrapy.item import Item, Field

class CraigslistSampleItem(Item):
    title = Field()
    link = Field()