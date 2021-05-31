# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


# 数据储存到WP_MySQL
class BeginPipeline:
    def process_item(self, item, spider):
        # 打印结果（可以在这个基础上继续创作）
        print(item)
        print(item['title'])
        print(item['content'])
        return item