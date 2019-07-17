class A():
    #构造函数 不应该有return
    def __init__(self,...):
    
    
    
    #不可以外部调用 私有函数 继承类也不可以调用 只能在类方法中调用
    def __a(self):
        print "__a"
    
    def _a(self):
        self.__a()
        print "_a"
     
