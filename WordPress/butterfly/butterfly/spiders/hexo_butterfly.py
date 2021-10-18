import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from butterfly.items import ButterflyItem


class HexoButterflySpider(CrawlSpider):
    # 项目名称
    name = 'hexo_butterfly'
    # 合法（允许）地址
    allowed_domains = ['www.kawashiros.club']
    # 初始启动地址
    start_urls = ['https://www.kawashiros.club/']

    rules = (
        Rule(LinkExtractor(allow=r'page/\d+/#content-inner'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        # 获取页面所有文章标签
        li_list = response.xpath('//*[@id="recent-posts"]/div')

        # 子增量
        o = 1

        for li in li_list:
            # //*[@id="recent-posts"]/div[1]/div[2]/a/@href
            # //*[@id="recent-posts"]/div[1]/div[2]/a
            link = 'https://www.kawashiros.club' + li.xpath('//*[@id="recent-posts"]/div[' + str(o) + ']/div[2]/a/@href').extract_first()

            o = o + 1
            # print(link)

            yield scrapy.Request(url=link, callback=self.parse_Content)

    def parse_Content(self, response):
        title = response.xpath('//*[@id="post-info"]/h1/text()').extract_first()
        data = response.xpath('//*[@id="post"]').extract_first()

        # 提交管道
        item = ButterflyItem()
        item['title'] = title
        item['data'] = data

        yield item