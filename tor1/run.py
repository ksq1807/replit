import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from view import userview
from tornado.options import define, options
import os
from util import utils

define("port", default=9000, help="run on the given port", type=int)


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [(r"/", userview.LoginHandler),
                    (r"/register", userview.RegisterHandler),
                    (r"/index", userview.IndexHandler),
                    (r"/updatepass", userview.ModifyPassWordHandler),
                    (r"/showall", userview.ShowAll),
                    (r"/showone/(\d+)", userview.ShowOne),]
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            # debug=True,
            xsrf_cookies=True,
            cookie_secret="shfueriterotjeirotueriotreuyewrosdjfsdgjsd"
        )
        tornado.web.Application.__init__(self, handlers, **settings)


if __name__ == "__main__":
    utils.logger.warning("正在监听9000端口")
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
