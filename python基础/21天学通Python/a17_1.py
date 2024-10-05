#使用 Flask 框架建立的一个最简单的 Web 程序
import flask #导入 flask
app = flask.Flask(__name__) #实例化主类 Flask
@app.route('/') #装饰器（实现 URL 地址）
def helo(): #定义业务函数
    return '你好，我是 Flask!' #返回字符串

app.run() #运行程序