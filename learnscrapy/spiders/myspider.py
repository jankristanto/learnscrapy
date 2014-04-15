from scrapy.spider import Spider
from scrapy.selector import HtmlXPathSelector

from learnscrapy.items import Project


class MySpider(Spider):
    name = "myspider"
    allowed_domains = ["wikipedia.org"]
    start_urls = [
	"http://www.wikipedia.org/"
    ]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)

        sites = hxs.select('//div[@class="otherprojects"]/div[@class="otherprojects-item"]')
        items = []

        for site in sites:
            item = Project()
            item['name'] = site.select('a/text()').extract()
            item['url'] = site.select('a/@href').extract()
            items.append(item)

        return items