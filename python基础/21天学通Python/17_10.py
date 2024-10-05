#用 Tornado 框架编写的最基本服务器程序
# -*- encoding:utf-8 -*-
import tornado.ioloop
import tornado.web
class MainHdl(tornado.web.RequestHandler): #自定义类
    def get(self): #回应 GET 请求方法
        self.write('你好，我是 Tornado!')
app = tornado.web.Application([
    (r'/',MainHdl), #URL 映射列表（可有多条）
    ],debug=True)

app.listen(8888) #服务器监听 8888 端口
tornado.ioloop.IOLoop.instance().start() #启动服务器