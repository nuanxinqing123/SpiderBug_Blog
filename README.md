＃SpiderBug_Blog（Scrapy博客爬虫）

学习Scrapy爬虫的一个🌰，用来针对各种博客主题的全站深度爬取。全站博文采集

## 注意事项

请在合法且博主允许的情况下辅助开发或者学习

* 一般主题都是一个样式，基本可以通用，但是不妨有些主题有多种样式。例如：Begin

## 开发进度

* WordPress（Begin）示例：https://gsbk.org/

    * 现在对于知更鸟只做个这种样式的爬取

## 修改处

    ```python
    # 遵守Reboot规则（settings.py）
    ROBOTSTXT_OBEY = True

    # 站点修改（每个spider文件夹里面Py文件里的第10行左右）
    allowed_domains = ['xxxx']
    start_urls = ['xxxx/page/2/']
    ```

## 笔记

目录下的`note.txt`是我的学习笔记，可以参考学习
