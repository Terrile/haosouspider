mkdir jobcache
mkdir data
scrapy crawl bingspider -s JOBDIR=jobcache --logfile=bingspider.log
#update the JOBDIR para according to http://stackoverflow.com/questions/27943970/how-to-limit-scrapy-request-objects
#according the refered url, the main purpose of jobdir is to limit the request num reside in memory