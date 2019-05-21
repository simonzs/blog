#coding:utf-8

import os
import json
import tornado.web

from api_gateway.settings import settings

class BaseHandler(tornado.web.RequestHandler):
    
    def set_default_headers(self):
        print('set_dafault_headers') 
        self.set_header('Content-Type', 'application/json; charset=UTF-8')

    def initialize(self, handler):
        # 对应每个请求的处理类Handler在构造一个实例后首先执行initialize()方法
        print("initialize: "+handler)
        self.handler = handler

    def prepare(self):
        print('prepare')
        if self.request.headers.get("Content-Type").startswith("application/json"):
            self.json_dict = json.loads(self.request.body)
        else:
            self.json_dict = None

    def finish_request(self, body): #若body是字典类型, write会自动将body序列化成json格式,并且,添加header头
        print("finish_request")
        # sort_keys是告诉编码器按照字典key排序(a到z)输出。
        # indent参数根据数据格式缩进显示，读起来更加清晰, indent的值，代表缩进空格式
        # separators参数的作用是去掉‘，’ ‘：’后面的空格，在传输数据的过程中，越精简越好，冗余的东西全部去掉。
        # skipkeys参数，在encoding过程中，dict对象的key只可以是string对象，如果是其他类型，那么在编码过程中就会抛出ValueError的异常。skipkeys可以跳过那些非string对象当作key的处理.
        # 输出真正的中文需要指定ensure_ascii=False
        self.write(json.dumps(body, sort_keys=True, indent=4, separators=(',',':'), skipkeys=False, ensure_ascii=False))
        self.finish()

    def write_success_json(self, data=None):
        self.set_status(200, 'OK')
        if data is None:
            return self.finish_request({'desc': 'success'})
        else:
            return self.finish_request({'desc': 'success', 'data':data})

    def new_url(self ,url):
        print('new_url')
        self.redirect(url)

    # send_error(status_code=500, **kwargs)
    # 抛出HTTP错误状态码status_code，默认为500，kwargs为可变命名参数。使用send_error抛出错误后tornado会调用write_error()方法进行处理，并返回给浏览器处理后的错误页面
    # 默认的write\_error()方法不会处理send\_error抛出的kwargs参数
    # 使用send_error()方法后就不要再向输出缓冲区写内容了！
    def write_error(self, status_code, **kwargs):
        # 用来处理send_error抛出的错误信息并返回给浏览器错误信息页面。
        # self.send_error(err_code, title=err_title, content=err_content)
        print('write_error')

        #self.write('title: {}, content: {}'.format(kwargs['title'], kwargs['content']))


class DemoHandler(BaseHandler):
    
    def get(self, url1, url2):
        print('get')
        print('url1: {}, url2:{}'.format(url1, url2))
        #data = get_query_argument(name="data") # this is a list
        #data = self.get_query_arguments(strip=True)
        data = self.get_query_arguments()
        self.do_get(data)

    def post(self):
        # self.get_arguments(name='data') # this is a list
        data = self.get_body_arguments(name='data', strip=True)
        self.do_post(data)

    def put(self):
        # self.get_arguments(name='data') # this is a list
        data = self.get_body_arguments(strip=True)
        self.do_put(data)

    def delete(self):
        data = self.get_query_argument(strip=True)
        self.do_delete(data)

    def do_get(self, data):
        print('do_get')
        print('method: {}'.format(self.request.method))
        print('host: {}'.format(self.request.host))
        print('uri: {}'.format(self.request.uri))
        print('path: {}'.format(self.request.path))
        print('query: {}'.format(self.request.query))
        print('version: {}'.format(self.request.version))
        #self.write('headers: '+ self.request.headers['Content-Type'])
        #self.write('headers: '+ str(self.request.headers.decode()))
        print('body: {}'.format(self.request.body.decode('utf-8')))
        if self.request.headers.get('Content-Type').startswith('application/json'):
            body = self.request.body.decode('utf-8')
            print('json body: {}'.format(json.loads(body)))
            #self.write('<br/> json.body: ' + json_args)
        print('remote_ip: {}'.format(self.request.remote_ip))

    def do_post(self, data):
        print('do_post')
        files = self.request.files
        file_load = files.get('img')
        if file_load:
            file =  file_load[0]
            body = img['body']
            name = img['filename']
            content_type = img['content_type']
            f = open(os.path.join(settings['path'], 'static', name), 'wb+')
            f.write(body)
            f.close()
