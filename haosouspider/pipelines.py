# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import codecs
from items import SearchResultItem

class DumpSearchResPipeline(object):
    def __init__(self):
        self.search_result = codecs.open('search_result.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        if isinstance(item,SearchResultItem):
            return self.process_searchRes(item,spider)

    def process_searchRes(self,item,spider):
        line = json.dumps(dict(item),ensure_ascii=False)+"\n"
        self.search_result.write(line)

    def spider_closed(self, spider):
        self.search_result.close()
