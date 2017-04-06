#! /usr/bin/env python
# coding: utf-8
# author:zhihua

import os
import sys
import socket
import redis
from tornado import httpserver, ioloop
from tornado import web
socket.setdefaulttimeout(0.3)
reload(sys)
sys.setdefaultencoding('utf-8')
settings = {
    'template_path': os.path.join(WEBUI_PATH, 'templates')
}
routes = [(r"/updatekey",      "dhandler.api.ApiUpdateHandler"),
          ]


class Application(web.Application):
    def __init__(self):
        web.Application.__init__(self, routes, **settings)
        self.redis = redis.StrictRedis(host=config.REDIS_HOST_TEST,
                                       port=config.REDIS_PORT,
                                       db=config.REDIS_DB_NUM,
                                       password=config.REDIS_PSWD)


def start():
    application = Application()
    http_server = httpserver.HTTPServer(application)
    http_server.listen(7652)
    ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    start()
