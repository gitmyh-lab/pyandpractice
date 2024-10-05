# -*- encoding:utf-8 -*-
import flask
app = flask.Flask(__name__)
@app.route('/hello')
def helo():
    return flask.render_template('index.html') #渲染 index.html 文件

app.run(debug=True)