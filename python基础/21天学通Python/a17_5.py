#获取 POST 请求参数
# -*- encoding:utf-8 -*-
import flask
html_txt = """ 
<!DOCTYPE html>
<html>
    <body>
        <h2>收到 GET 请求</h2>
        <form method='post'>
        <input type='text' name='name' placeholder='请输入你的姓名' />
        <input type='submit' value='发送 POST 请求' />
        </form>
    </body>
</html>
"""
app = flask.Flask(__name__)
@app.route('/hello',methods=['GET','POST'])
def helo():
    if flask.request.method == 'GET':
        return html_txt
    else:
        #获取参数 name 的值
        #为'name' in flask.request.form 为 False 时，无论 and
        #后表达式值为何种情况，结果为 False，所以只返回 False。
        #如果'name' in flask.request.form 为
        #True 时，整个逻辑运算结果就取决于第二个表达式的值，
        #所以会返回 flask.request.form['name']的值
        name = 'name' in flask.request.form and flask.request.form['name']
        if name:
            return '你是：' + name + '!'
        else:
            return '你没有输入姓名！'

app.run(debug=True)