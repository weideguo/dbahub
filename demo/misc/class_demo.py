class A(B):
    #构造函数 不应该有return
    def __init__(self,...):
    
    
    
    #不可以外部调用 私有函数 继承类也不可以调用 只能在类方法中调用
    def __a(self):
        print "__a"
    
    #可以外部调用 继承
    def _a(self):
        self.__a()
        print "_a"

        #调用父方法
        super(A,self).__init__()
    

       
        
        
#多重继承
class D(E,F)
    pass
        
        
#Method Resolution Order(方法解析顺序) 
#查看D的mro        
D.mro()     

#super(cls, inst) 获得的是 cls 在 inst 的 MRO 列表中的下一个类
#super函数的工作原理
def super(cls,inst):
    mro=inst.__class__.mro()
    return mro[mro.index(cls)+1]
    
    
    
__class__ 获取实例对应的类
    
