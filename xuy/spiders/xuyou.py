# -*- coding: utf-8 -*-
import scrapy


class XuyouSpider(scrapy.Spider):
    name = 'xuyou'
    allowed_domains = ['https://blog.youxu.info/archive.html']
    start_urls = ['https://blog.youxu.info/archive.html']

    def parse(self, response):

    	title=response.xpath("/html/body/div[2]/div/div[2]/div/ul/li/a/text()")
    	
    	with open('titles.txt','w') as f:
    		
    		for tt in title:
    			m=tt.extract()
    			f.write(m)
    			f.write('\n')

    	print ("it is completed")
    		


        
