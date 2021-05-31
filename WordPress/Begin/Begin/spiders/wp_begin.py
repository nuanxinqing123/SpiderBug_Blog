import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from Begin.items import BeginItem, BeginContent


class WpBeginSpider(CrawlSpider):
    name = 'wp_begin'
    allowed_domains = ['gsbk.org']
    start_urls = ['https://gsbk.org/page/2/']

    rules = (
        Rule(LinkExtractor(allow=r'page/\d+/'), callback='parse_item', follow=False),
        Rule(LinkExtractor(allow=r'\d\.html'), callback='parse_Content', follow=False),
    )

    def parse_item(self, response):
        # 获取页面所有文章标签
        li_list = response.xpath('/html/body/div[1]/div[2]/div[1]/main/article')

        # 增量
        o = 1

        # 遍历文章
        for li in li_list:
            # 获得Page页面的Link
            # /html/body/div[1]/div[3]/div[1]/main/article[1]/header/h2/a
            link = li.xpath('/html/body/div[1]/div[2]/div[1]/main/article[' + str(o) + ']/header/h2/a/@href').extract_first()

            # 自增加
            o += 1

            # 提交管道
            item = BeginItem()
            item['link'] = link

            yield item

    def parse_Content(self,response):
        # 获取文章正文内容
        title = response.xpath('/html/body/div[1]/div[2]/div[1]/main/article/header/h1/text()').extract_first()
        content = response.xpath('/html/body/div[1]/div[2]/div[1]/main/article/div/div[2]').extract_first()
        # print(content)

        # 提交管道
        item = BeginContent()
        item['content'] = content
        item['title'] = title

        yield item


