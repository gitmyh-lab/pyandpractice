# -*- encoding:utf-8 -*-
import flask
html_txt = """
<!DOCTYPE html>
<html>
    <body>
        <h2>收到 GET 请求</h2>
        <a href='/get_info'>获取会话信息</a>
    </body>
</html>
"""
app = flask.Flask(__name__)
@app.route('/set_info/<name>')
def set_cks(name):
    name = name if name else 'anonymous'
    flask.session['name'] = name #设置 session
    return html_txt
@app.route('/get_info')
def get_cks():
    name = 'name' in flask.session and flask.session['name'] #获取 session
    if name:
        return '获取的会话信息是:' + name
    else:
        return '没有相应会话信息。'

app.secret_key = 'dfadff#$#5dgfddgssgfgsfgr4$T^%^' #设置 cookie 密钥
app.run(debug=True)