# Impoorting all the required modules
from scrapy.item import  Field
from scrapy.item import Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.loader.processors import MapCompose
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader

# This class covers the Article items from the IGN website
class Article(Item):
    title = Field()
    content = Field()

# This class covers the Reviews items from the IGN website
class Review(Item):
    title = Field()
    rating = Field()

# This class covers the Video items from the IGN website
class Video(Item):
    title = Field()
    date_release = Field()

# This sections creates the main crawler
class IGNCrawler(CrawlSpider):
    name = 'ign'
    # These settings include the User agent to avoid detection and the count of items scraped
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
                      AppleWebKit/537.36 (KHTML, like Gecko)\
                       Chrome/80.0.3987.149 Safari/537.36',
        'CLOSESPIDER_PAGECOUNT': 50
    }
    # The delay of seconds for each request
    download_delay = 1
    # The allowed domains 
    allowed_domains = ['latam.ign.com']
    # This URL includes a specific category related to video games
    start_urls = ['https://latam.ign.com/se/?model=article%2Cvideo&order_by=-date&q=ps4']

    rules = (
        # This rule is declared in order to detect the horizontal behaivor of the website (if the website is in the Articles, Reviews o Videos)
        Rule(
            LinkExtractor(
              allow=r'type='
            ), follow=True
        ),
        # This rule helps to make the horizontal exploration of data according to the pagination of the website
        Rule(
            LinkExtractor(
                allow=r'&page=\d+'
            ), follow=True, callback='parse_items'
        ),
        # This rule specifically evaluates the Reviews
        Rule(
            LinkExtractor(
                allow=r'/review/'
            ), follow=True, callback='parse_review'
        ),
        # This rule specifically evaluates the Videos
        Rule(
            LinkExtractor(
                allow=r'/video/'
            ), follow=True, callback='parse_video'
        ),
        # This rule specifically evaluates the Articles/News
        Rule(
            LinkExtractor(
                allow=r'/news/'
            ), follow=True, callback='parse_news'
        ),
    )
    # Declares a simple function to clean the content
    def clean_text(self, text):
        new_text = text.replace('\n', ' ').replace('\r', ' ').replace('\t', ' ').strip()
        return new_text
    # This callback gets the information for the Article Item by using xPath
    def parse_news(self, response):
        item = ItemLoader(Article(), response)
        item.add_xpath('title', '//h1/text()')
        item.add_xpath('content', '//div[@id="id_text"]//*/text()')

        yield item.load_item()
    # This callback gets the information for the Review Item by using xPath
    def parse_review(self, response):
        item = ItemLoader(Review(), response)
        item.add_xpath('title', '//h1/text()')
        item.add_xpath('rating', '//span[@class="side-wrapper side-wrapper hexagon-content"]/text()')

        yield item.load_item()
    # This callback gets the information for the Video Item by using xPath
    def parse_video(self, response):
        item = ItemLoader(Video(), response)
        item.add_xpath('title', '//h1/text()')
        item.add_xpath('date_release', '//span[@class="publish-date"]/text()')

        yield item.load_item()