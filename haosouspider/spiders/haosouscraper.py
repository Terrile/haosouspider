# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import HtmlXPathSelector
from scrapy.selector import Selector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.http import Request
import string
import re
import math
import urllib
from scrapy import log
from pprint import pprint
from ..items import HaosouspiderItem
import urllib2
import codecs
TASK_INPUT_FILE = './task/task.txt'
class HaosouSpider(scrapy.Spider):
    name = "bingspider"
    allowed_domains = ["bing.com"]
    start_urls = []
    target_site = 'vdisk.weibo.com'
    def __init__(self):
        taskfile = codecs.open(TASK_INPUT_FILE,mode='r',encoding='utf-8')
        query_list=taskfile.readlines()
        for query in query_list:
            query=query.strip('\n\r\t').encode('utf-8')
            title = urllib2.quote(query)
            query_url='http://www.haosou.com/s?q='+title+' site:'+self.target_site
            self.start_urls.append(query_url)
        taskfile.close()

    def parse(self, response):
        html_txt = response.body.decode("utf-8","ignore")
       # print html_txt
        hxs = Selector(text=html_txt)
        items = hxs.xpath('//ol[@id="m-result"]/li[@class="first"]')
        query = response.url

        if items:
            rank = 0
            for item in items:
                title = item.xpath('.//h3[@class="res-title"]/a')
                url = item.xpath('.//h3[@class="res-title"]/a/@href')
                caption = item.xpath('.//p[@class="res-desc"]/p')
                search_res = HaosouspiderItem()
                search_res['query'] = query
                search_res['title'] = title.select('string()').extract()[0]
                search_res['url'] = url.extract()[0]
                search_res['caption'] = caption.select('string()').extract()[0]
                search_res['rank'] = rank
                rank+=1
                yield  search_res
        else:
            print 'search results not found'