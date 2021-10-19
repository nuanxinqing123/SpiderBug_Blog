# SpiderBug_Blog（Scrapy博客爬虫）

学习Scrapy爬虫的一个🌰，用来针对各种博客主题的全站深度爬取。全站博文采集

## 注意事项

请在合法且博主允许的情况下辅助开发或者学习

* 一般主题都是一个样式，基本可以通用，但是不妨有些主题有多种样式。例如：Begin
* Typecho程序的handsome主题文章末尾有转载说明，建议保留。[不需要请自行删除 blockquote 标签的内容]

## 开发进度

* WordPress（Begin）示例：https://www.sevesum.com/

    * 现在对于知更鸟只做个这种样式的爬取
  
* Typecho（handsome） 示例：https://blog.say521.cn/
* Hexo(Butterfly) 示例：https://www.kawashiros.club/
* Hexo(Fluid) 示例：https://blog.6yfz.cn/

## 安装模块

使用PyCharm在项目根目录下打开终端以此执行以下命令，安装所需要的包

  ```
  pip3 install scrapy
  pip3 install -r requirements.txt
  ```

## 修改处

    ```python
    # 遵守Reboot规则（settings.py）
    ROBOTSTXT_OBEY = True

    # 站点修改（每个spider文件夹里面Py文件里的第10行左右）
    allowed_domains = ['xxxx']
    start_urls = ['xxxx/page/2/']

    # 全站爬取开关
    项目spider目录下的文件中的 ’follow=False‘ 值
    False为关， True为开
    ```

## 笔记

目录下的`note.txt`是我的学习笔记，可以参考学习，`Scrapy_Setting.txt`是关于Scrapy的Settings.py的配置文档，搭配使用
