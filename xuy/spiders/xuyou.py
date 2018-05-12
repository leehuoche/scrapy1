# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from urllib import parse


class XuyouSpider(scrapy.Spider):
    name = 'xuyou'
    allowed_domains = ['blog.youxu.info']
    start_urls = ['https://blog.youxu.info/page2/']


    def parse(self,response):

        title=response.xpath("/html/body/div[2]/div/div[2]/div[1]/div/h1/a/text()").extract()[0]
        first_par=response.xpath("/html/body/div[2]/div/div[2]/div[1]/div/div/p/text()").extract()[0]
        name=response.url.split('/')[-2]
        f_name=name+'.txt'

        with open(f_name,'a+') as f:
            f.write(title)
            f.write('\n')
            f.write(first_par)
            f.write('\n')

        next_url=response.xpath("/html/body/div[2]/div/div[2]/div[6]/a[2]//@href").extract()[0]
        yield Request(url=parse.urljoin(response.url,next_url),callback=self.parse)





    










    

    		


        
