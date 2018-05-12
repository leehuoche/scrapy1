# scrapy1
这个项目是用scrapy建立的爬虫。作为实际的演示，抓取了我最喜爱的一个博客--徐宥的博客`https://blog.youxu.info`。并打印了他所发表的文章的标题。


使用此项目首先需要安装scrapy:`pip install scrapy`

在项目的根目录下，使用shell命令：`scrapy crawl xuyou`即可。


标题的结果放在文件 `titles.txt`.

本次可以将标题打印为单个的`txt`文档.


# 过程体会
1. 爬虫的制作一般步骤为 对目标网页发送请求，下载网页，解析网页，对解析出的字段进行存储或者处理。


0. scrapy 是python的一个强大的框架，用于制作爬虫。在这个框架里面可以使用各种python的库，在解析网页时候使用`xpath`和`css`，简化了许多步骤。

0. 在shell中使用`scrapy shell + 网址` 可以在解析字段时候更为方便的测试语句的正确性。


# 自动爬取下一页
使用`Request` 中的`callback` 回调`parse`函数即可。

# 下一步待优化
将提取的数据放到数据库里
