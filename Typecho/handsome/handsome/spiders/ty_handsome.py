import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from handsome.items import HandsomeItem


class TyHandsomeSpider(CrawlSpider):
    name = 'ty_handsome'
    allowed_domains = ['blog.say521.cn']
    start_urls = ['https://blog.say521.cn/page/1/']

    rules = (
        Rule(LinkExtractor(allow=r'page/\d+/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        # 获取页面文章地址
        li_list = response.xpath('/html/body/div[1]/div/main/div/div/div/div/div')

        # 自增值
        o = 1

        # 遍历地址
        for i in li_list:
            #   /html/body/div[1]/div/main/div/div/div/div/div[1]/div[2]/h2/a
            #   /html/body/div[1]/div/main/div/div/div/div/div[2]/div[2]/h2/a
            link = i.xpath('/html/body/div[1]/div/main/div/div/div/div/div[' + str(o) + ']/div[2]/h2/a/@href').extract_first()

            # 自增
            o += 1

            # 提交深度爬取
            yield scrapy.Request(url=link, callback=self.hanSomeSpider)

    def hanSomeSpider(self, response):
        # 获取标题
        title = response.xpath('/html/body/div[1]/div/main/div/div/header/h1/text()').extract_first()
        # 获取正文
        data = response.xpath('/html/body/div[1]/div/main/div/div/div[2]/div[1]/article/div/div[1]').extract_first()

        # 提交管道
        item = HandsomeItem()
        item['title'] = title
        item['data'] = data

        yield item
