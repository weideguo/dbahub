#encoding = utf-8

from werkzeug.wsgi import DispatcherMiddleware
from werkzeug.serving import run_simple
from flask import Flask
from app1 import app as app1
from app2 import app as app2

app = Flask(__name__)
app.secret_key = 'topLevel'

@app.route('/')
def index():
    return 'Hello top level!'

app = DispatcherMiddleware(app,{
    '/app1':     app2,
    '/app2':     app1
})

if __name__ == '__main__':
    run_simple('localhost', 5000, app,
               use_reloader=True, use_debugger=True, use_evalex=True)