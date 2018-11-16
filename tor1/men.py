import memcache  # 链接

mc = memcache.Client(['192.168.50.205:11211'])
# mc = memcache.Client([('192.168.50.205:11211', 1), ('192.168.50.206:11211', 2), ('192.168.50.207:11211', 3)])
# 插入
# mc.set("aaa", "rrrrr",time=2)
# 读取
ret = mc.get('aaa')
print(ret)
