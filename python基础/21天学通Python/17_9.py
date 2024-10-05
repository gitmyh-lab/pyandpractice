# -*- encoding:utf-8 -*-
import flask
app = flask.Flask(__name__)
@app.route('/upload',methods=['GET','POST']) #请求的 GET、POST 映射同一函数
def upload():
    if flask.request.method == 'GET':
        return flask.render_template('upload.html') #请求方法为 POST 时返回上传页面
    else:
        file = flask.request.files['file'] #获取文件对象
        if file: #如果文件不是空
            file.save(file.filename) #保存文件（以传来的文件名）
            return '上传成功！'

app.run(debug=True)