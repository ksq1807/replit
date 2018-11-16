import memcache  # 链接
import config
try:
    mc = memcache.Client(config.Men.url)
except Exception as e:
    print(e)
