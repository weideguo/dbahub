#coding:utf8
#路由样例

route_list=[]

def route(path=None, callback=None):
    def decorator(callback):
        route_list.append((path,callback))
        return callback
        
    return decorator(callback) if callback else decorator
        
        
        
#######################################


@route('/hello/<name>')
def index(name):
    print name
  
  
print  route_list
