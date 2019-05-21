#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import tornado.web
from api_gateway.urls import url_patterns
from api_gateway.settings import settings


class TornadoApplication(tornado.web.Application):
    
    def __init__(self):
        tornado.web.Application.__init__(self, url_patterns, **settings)
        
def main():
    app = TornadoApplication()
    # listen(端口)方法用来创建一个http服务器实例，并绑定到给定端口（注意：此时服务器并未开启监听）
    app.listen(tornado.options.options.port) 
    #http_server = tornado.httpserver.HTTPServer(app)
    #http_server.bind(tornado.options.options.port) #将服务器绑定到指定端口
    #http_server.start(12)
    tornado.ioloop.IOLoop.current().start()
