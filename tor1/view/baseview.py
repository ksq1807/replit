import tornado.web
from util import utils


class BaseView(tornado.web.RequestHandler):
    def prepare(self):
        remote_ip = self.request.remote_ip
        num = 0
        try:
            num = int(utils.getMem(remote_ip))
        except Exception as e:
            utils.logger.error(e)
        if num == 0:
            utils.setMem(remote_ip, values=str(num + 1), time=24 * 3600)
        elif num < 60:
            utils.setMemReplace(remote_ip, values=str(num + 1))
        else:
            self.write_error(404)
            # print(remote_ip)
