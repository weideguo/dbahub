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
    response=make_response('Hello World')
    
    #header
    response.headers['Access-Control-Allow-Origin'] = '192.168.*.*'   
 
    #cookie
    response.set_cookie('kkkkk','vvvvv')        #设置cookie    JS获取cookie:  document.cookie 
    outdate=datetime.datetime.today() + datetime.timedelta(days=30)  
    response.set_cookie('kkkkk222','vvvvv222',expires=outdate)
    return response  	


@app.route('/get/')
def test2():
    print request.cookies         
    print request.headers
    print request.args
    a=session.get('username')  
    return a


"""
http header不分大小写 域名不分大小写 url区分大小写
content-type      
application/x-www-form-urlencoded  数据被编码为名称/值对。这是标准的编码格式。
multipart/form-data                数据被编码为一条消息，页上的每个控件对应消息中的一个部分。
text/plain                         数据以纯文本形式(text/json/xml/html)进行编码，其中不含任何控件或格式字符。postman软件里标的是RAW。
"""

@app.route('/post/',methods=['GET','PUT','POST'])
def test3():
    """
    curl $root_url"/post/" -d "a=aaaa&b=bbbbb"  -H "Content-Type:application"
    curl $root_url"/post/" -d "{\"a\":\"aaaaa\"}"  -H "Content-Type:application"
    content-type 不为 application/x-www-form-urlencoded 即可
    """
    print request.method
    print request.url
    print request.headers
    print request.data
    print request.get_data()
    return "post success"

@app.route('/post1/',methods=['GET','PUT','POST'])
def test31():
    """
    curl $root_url"/post1/" -d "{\"a\":\"aaaaa\"}"  -H "Content-Type:application/json"
    """
    print request.headers
    print request.json
    print request.get_json()
    return "post success"

@app.route('/post2/',methods=['GET','PUT','POST'])
def test32():
    """
    curl $root_url"/post2/" -d "{\"a\":\"aaaaa\"}"
    curl $root_url"/post2/" -d "a=aaaa&b=bbbbb" 
    默认 Content-Type: application/x-www-form-urlencoded
    """
    print request.headers
    print request.form
    return "post success"



@app.route('/upload/',methods=['GET','PUT','POST'])
def test4():
    """
    curl "http://this_host/upload/" -F "filename=@/root/x.txt"  
    Content-Type: multipart/form-data; 
    """
    print request.headers
    file = request.files.get('filename')
    file.save('/tmp/aaa.txt')
    return "uploal success"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)
    #app.run(host="0.0.0.0", port=4000, threaded=False)

