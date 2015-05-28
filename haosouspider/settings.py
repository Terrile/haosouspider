# -*- coding: utf-8 -*-

# Scrapy settings for haosouspider project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'haosouspider'

SPIDER_MODULES = ['haosouspider.spiders']
NEWSPIDER_MODULE = 'haosouspider.spiders'
DOWNLOADER_MIDDLEWARES = {
        'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware' : None,
        'haosouspider.rotate_useragent.RotateUserAgentMiddleware' :400
    }
ITEM_PIPELINES = ['haosouspider.pipelines.DumpSearchResPipeline']
DOWNLOAD_DELAY = 2
COOKIES_ENABLED = False
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'haosouspider (+http://www.yourdomain.com)'
