import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from Fluid.items import FluidItem


class HexoFluidSpider(CrawlSpider):
    name = 'hexo_fluid'
    allowed_domains = ['blog.6yfz.cn']
    start_urls = ['https://blog.6yfz.cn/']

    rules = (
        Rule(LinkExtractor(allow=r'page/\d+/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        # 获取页面Link
        li_list = response.xpath('//*[@id="board"]/div/div/div/div')

        o = 1

        for li in li_list:
            # //*[@id="board"]/div/div/div/div[2]/article/h1/a
            link = 'https://blog.6yfz.cn' + li.xpath(
                '//*[@id="board"]/div/div/div/div[' + str(o) + ']/article/h1/a/@href').extract_first()

            o += 1

            yield scrapy.Request(url=link, callback=self.parse_Context)

    def parse_Context(self, response):
        title = response.xpath('//*[@id="subtitle"]/@title').extract_first()
        context = response.xpath('//*[@id="board"]/article/div[1]').extract_first()

        item = FluidItem()
        item['title'] = title
        item['context'] = context

        yield item
