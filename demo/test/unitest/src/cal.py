#coding:utf8
class Calc(object):
    def add(self, x, y):
        # 加法计算
        result = x + y
        return result

    def sub(self, x, y):
        # 减法计算
        result = x - y
        return result

    @classmethod
    def mul(cls, x, y):
        # 乘法计算
        result = x * y
        return result
        
        
if __name__=="__main__":
    c=Calc()
    print (c.add(1,2))
    print (c.sub(5,2))
