#coding:utf-8
#pip install web.py

import web

urls = (
    '/(.*)', 'hello'
)
app = web.application(urls, globals())

class hello:
    def GET(self, name):
        if not name:
            name = 'World'
        return 'Hello, ' + name + '!'

if __name__ == "__main__":
    app.run()
    
    
#python webpy_demo.py 1234
#curl "http://127.0.0.1:1234/www"