# -*- encoding:utf-8 -*-
import flask

html_txt = """
<!DOCTYPE html>
<html>
    <body>
        <h2>收到 GET 请求</h2>
        <a href='/get_info'>获取 cookie 信息</a>
    </body>
</html>
"""
app = flask.Flask(__name__)


@app.route('/set_info/<name>')  # 从 URL 中获取参数 URL 装饰器
def set_cks(name):
    name = name if name else 'anonymous'
    # resp = make_response(content) #content 返回页面内容
    resp = flask.make_response(html_txt)  # 构造响应对象
    resp.set_cookie('name', name)  # 设置 cookie
    return resp


@app.route('/get_info')
def get_cks():
    name = flask.request.cookies.get('name')  # 获取 cookie 信息
    return '获取的 cookie 信息是:' + name  # 返回带 cookie 信息的页面内容


app.run(debug=True)