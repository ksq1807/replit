from myproject.utils import util

url = "https://news.suning.com/whaohuo.html"
header = {
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding":"gzip, deflate, br",
    "Accept-Language":"zh-CN,zh;q=0.9",
    "Connection":"keep-alive",
    "Host":"news.suning.com",
    "If-None-Match":'W/"9cef-Pv8YCTy1hw/AJeJmuZ1GnWnZXyk"',
    "Upgrade-Insecure-Requests":"1",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36"
}
body = util.get(url=url)
print(body[2])





