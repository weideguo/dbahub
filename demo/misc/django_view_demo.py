from rest_framework.views import APIView
import time
visit_record = {}

"""
django访问频率限制
"""


class MyThrottle(object):
    # 10秒访问3次
    VISIT_TIME = 10
    VISIT_COUNT = 3
    
    # 固定函数
    def allow_request(self, request, view):
        # 获取登录主机的id 
        id = request.META.get('REMOTE_ADDR')
        self.now = time.time()

        if id not in visit_record:
            visit_record[id] = []

        self.history = visit_record[id]
        
        while self.history and self.now - self.history[-1] > self.VISIT_TIME:
            self.history.pop()
        
        if len(self.history) >= self.VISIT_COUNT:
            return False
        else:
            self.history.insert(0, self.now)
            return True
    
    # 固定函数
    def wait(self):
        return self.history[-1] + self.VISIT_TIME - self.now
        
        

class AnyLogin(APIView):
    permission_classes = ()
    authentication_classes = ()

    throttle_classes = [MyThrottle,]


    def get(self, request, args = None):
        pass

    def post(self, request, args = None):
        pass

    def put(self, request, args = None):
        pass

    def delete(self, request, args = None):
        pass




