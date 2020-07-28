# -*- coding: utf-8 -*-
import scrapy
from baiducrawler.items import BaiducrawlerItem
list1=[]
class GithubSpider(scrapy.Spider):
    name = 'github'
    allowed_domains = ['github.com']
    start_urls=["https://github.com/f-droid/fdroiddata/tree/master/metadata"]
    def parse(self, response):
        print('=' * 40)
        ymllist = response.xpath(
            "// *[contains(@title,'yml')]/@href").extract()
        for yml in ymllist:
            yield scrapy.Request(url = "https://github.com"+yml, callback=self.new_parse)
            print(yml + "\n")
        # yield scrapy.Request(url="https://github.com" + ymllist[0], callback=self.new_parse)
        # print(ymllist)
        #
        # items1 = []
        # item = BaiducrawlerItem(ymllist=ymllist)
        # items1.append(item)
        # print('+' * 40)
        # return items1
    
    def new_parse(self, response):
        print('=' * 40)
        print(response)
        content1 = response.xpath(
            "//*[text()[contains(.,'https://git')]]/text()"
        ).extract()
        content = response.xpath(
            "//*[text()[contains(.,'https://git')]]/text()"
        ).extract()
        
        suffix="fdroiddata"
        suffix1="https://github"
        suffix2="https://gitlab"
        # if(content.endswith(suffix)):
        #     return
        # if content.startswith(suffix1) or content.startswith(suffix2)
        try:
            if (content[1].endswith(suffix)):
                return
            print(content1)
            print(content[1])
            list1.append(content[1])
            print(list1)
            # yield scrapy.Request(url=content + "/blob/master/project/app/build.gradle", callback=self.new_parse1)
        except:
            return
        # items1 = []
        # item = BaiducrawlerItem(list1=list1)
        # items1.append(item)
        # print('+' * 40)
        # return items1
       
    
    def new_parse1(self,response):
        handle_httpstatus_list = [404, 500]
        if response.status in handle_httpstatus_list:
            return
        try:
            txt=response.xpath("//*[@id='js-repo-pjax-container']/div[3]/div/div[3]/div[2]/table/tbody").extract()
            print(txt)
        except:
            pass
        pass