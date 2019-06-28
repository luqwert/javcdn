# -*- coding: utf-8 -*-

# Scrapy settings for JavSpider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

HEADERS = {
    r'cookie': '__cfduid=d761cee020cec276f507132139addc7421545555734; __guid=35400359.4113806376697964000.1545555738264.177; HstCfa4127494=1545555756697; HstCmu4127494=1545555756697; PHPSESSID=6ln21mg1n6nrhc3m5t9q9eqt04; starinfo=glyphicon%20glyphicon-plus; 4fJN_2132_saltkey=HJJ2dBHW; 4fJN_2132_lastvisit=1546156644; 4fJN_2132_sid=TRLVHQ; 4fJN_2132_lastact=1546160245%09misc.php%09seccode; 4fJN_2132_seccode=7942.ba32df629914d0e609; HstCnv4127494=3; HstCns4127494=7; monitor_count=136; HstCla4127494=1546171197997; HstPn4127494=74; HstPt4127494=137; existmag=all',
}

BOT_NAME = 'JavSpider'

SPIDER_MODULES = ['JavSpider.spiders']
NEWSPIDER_MODULE = 'JavSpider.spiders'

LOG_LEVER = 'WORNING'
LOG_FILE = './log.log'
# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

REDIS_URL = 'redis://127.0.0.1:6379'
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
SCHEDULER_PERSIST = False


# COMMANDS_MODULE = 'JavSpider.commands'
# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = True
COOKIES = {'4fJN_2132_lastact': '1546160245%09misc.php%09seccode', 'HstCla4127494': '1546171197997', 'existmag': 'all', 'PHPSESSID': '6ln21mg1n6nrhc3m5t9q9eqt04', 'HstPt4127494': '137', '__guid': '35400359.4113806376697964000.1545555738264.177', '4fJN_2132_seccode': '7942.ba32df629914d0e609', 'HstCfa4127494': '1545555756697', 'starinfo': 'glyphicon%20glyphicon-plus', '4fJN_2132_lastvisit': '1546156644', '4fJN_2132_sid': 'TRLVHQ', '__cfduid': 'd761cee020cec276f507132139addc7421545555734', 'HstPn4127494': '74', 'monitor_count': '136', '4fJN_2132_saltkey': 'HJJ2dBHW', 'HstCnv4127494': '3', 'HstCmu4127494': '1545555756697', 'HstCns4127494': '7'}

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'JavSpider.middlewares.JavspiderSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'JavSpider.middlewares.JavspiderDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'JavSpider.pipelines.JavspiderPipeline': 300,
    'scrapy_redis.pipelines.RedisPipeline': 400,

}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
