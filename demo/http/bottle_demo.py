#coding:utf-8

from bottle import route, run, template

@route('/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

run(host='localhost', port=1234)

