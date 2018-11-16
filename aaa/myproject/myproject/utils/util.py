# 用于自定义的包
import requests
import logging
import uuid
logging.basicConfig(level = logging.INFO,format = '[%(asctime)s-%(name)s-%(levelname)s-%(filename)s-%(lineno)d]%(message)s')
logger = logging.getLogger(__name__)

def get(url, params=None, cookie=None, headers=None, proxies=None):
    '''
    此方法用于发起get请求
    :param url:  网址
    :param params:  网址问号后的参数
    :param cookie:  cookie 用于模拟登录
    :param headers:   网址的头文件
    :param proxies:   网络代理
    :return:
    '''
    s = requests.session()
    try:
        if params != None:
            s.params = params
        if cookie != None:
            s.cookies = cookie
        if headers != None:
            s.headers = headers
        if proxies != None:
            s.proxies = proxies
        # 设置过期时间
        r = s.get(url=url, timeout=20)
        return (1, r.content, r.text)
    except Exception as e:
        print(e)
    finally:
        if s:
            s.close()
    return (0,)


def post(url, data, params=None, cookie=None, headers=None, proxies=None):
    '''
    此方法用于发起post请求
    :param url:
    :param data:  post 请求中的from data
    :param params:
    :param cookie:
    :param headers:
    :param proxies:
    :return:
    '''
    s = requests.session()
    try:
        if params != None:
            s.params = params
        if cookie != None:
            s.cookies = cookie
        if headers != None:
            s.headers = headers
        if proxies != None:
            s.proxies = proxies
        r = s.post(url=url, data=data, timeout=20)
        return (1, r.content,r.text,r.cookies)
    except Exception as e:
        print(e)
    finally:
        if s:
            s.close()
    return (0,)


# 用于生成随机字符串，在高并发时，主键不会重复，异步时也会使用这个方法
def getUUID():
    return str(uuid.uuid4())
# 用于去除爬取内容的特殊符号
def getBody(body):
    return body.replace("'","‘")




