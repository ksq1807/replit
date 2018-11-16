# -*- coding: utf-8 -*-

# Scrapy settings for myproject project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'myproject'

SPIDER_MODULES = ['myproject.spiders']
NEWSPIDER_MODULE = 'myproject.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
# 用于伪造浏览器
#USER_AGENT = 'myproject (+http://www.yourdomain.com)'

# Obey robots.txt rules
# ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# 并发的请求总数，即同一时刻发起的请求
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 1  # 请求延迟，相当于time.sleep(3)
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16  # 对同一个网站的设定
# CONCURRENT_REQUESTS_PER_IP = 3  # 对同一个IP的设定，并发的请求量，优先级高与网站的

# Disable cookies (enabled by default)
# 是否要启用cookie的中间键，发送请求时，都会携带cookie，使用要慎重
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# 是否启用布尔值，启用远程终端
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# 默认的请求头文件
# DEFAULT_REQUEST_HEADERS =  {  # 默认的请求头
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
#     "Accept-Encoding": "gzip, deflate, br",
#     "Accept-Language": "zh-CN,zh;q=0.9",
#     "Connection": "keep-alive",
#     "Cookie": "antipas=2192r893U97623019B485050817",
#     "Host": "www.guazi.com",
#     "Referer": "https://www.guazi.com/sjz/dazhong/",
#     "Upgrade-Insecure-Requests": "1",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
# }

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# 蜘蛛的中间键，可以自己设定,后面的值为权重，越小越优先
#SPIDER_MIDDLEWARES = {
#    'myproject.middlewares.MyprojectSpiderMiddleware': 543,
#    #'myproject.middlewares.aa': 1000,

#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
# 下载器的中间键，一旦设定就变成了但进程的设定
#DOWNLOADER_MIDDLEWARES = {
#    'myproject.middlewares.MyprojectDownloaderMiddleware': 543,
#    # 'myproject.middlewares.MyprojectDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# 管道配置，用于将数据存储的位置，可以是mongo，MySQL或是其他
ITEM_PIPELINES = {
   'myproject.pipelines.MyprojectPipeline': 300,
   #'myproject.pipelines.Myproject333Pipeline': 400,
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
# 配置数据库相关的信息
MONGOHOST = "127.0.0.1"
MONGOPORT = 27017
MONGODB = "guazi"
# 确保蜘蛛通过redis共享相同的重复过滤器，即实现去重的功能
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
# 重写调度器，使用redis中启用调度存储请求队列
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# 不清除redis队列，允许暂停，恢复抓取
SCHEDULER_PERSIST = True
# 连接到redis数据库
REDIS_HOST = "127.0.0.1"
REDIS_PORT = 6379
# 用于指定数据库
REDIS_PARAMS = {"db":2}









