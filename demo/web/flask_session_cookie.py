#coding:utf8
import os
import datetime
from datetime import timedelta
from flask import Flask,session,request,Response,make_response


app = Flask(__name__)
#必须设置SECRET_KEY才能使用session
#app.config['SECRET_KEY'] = os.urandom(24)
app.config['SECRET_KEY'] = '0b70c728603511e9afd3000c295dd589'
#设置session的有效期
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours=2)
#flask的session通过cookie存储在客户端  但用 document.cookie看不到 设置了httponly脚本不可访问
#其他web服务可能存储在服务端


@app.route('/set/<username>')
def test1(username):
    session['username'] = username
    response=make_response('Hello World');
    response.set_cookie('kkkkk','vvvvv')                                 #设置cookie    JS获取cookie:  document.cookie 
    #outdate=datetime.datetime.today() + datetime.timedelta(days=30)     #默认为浏览回话结束 即关闭浏览器后清除
    #response.set_cookie('kkkkk222','vvvvv222',expires=outdate)
    return response


@app.route('/get/')
def test2():
    print request.cookies
    print request.headers
    a=session.get('username')
    return a


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)
