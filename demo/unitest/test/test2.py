#coding:utf8
import unittest
import random
from src.cal import Calc

class CalcTest(unittest.TestCase):
    #执行测试用例前的准备操作，每个测试用例执行前都会被执行
    def setUp(self):
        self.cal = Calc()
        print ("setup completed!")

    def test_add(self):
        result = self.cal.add(1,2)
        self.assertTrue(result==3)
        #assert 3==result
              
    def test_sub(self):
        result = self.cal.sub(5,1)
        self.assertTrue(result==4)
    
        '''
        常用断言
        assertTrue 表达式是否为True或者False
        assertEqual 元素是否相等
        '''

    #执行完测试用例后的清理操作，每个测试用例执行完都会被执行
    def tearDown(self):
        print ("tearDown completed")

    
    @classmethod
    def setUpClass(cls):
        '''
        一个类方法在单个类测试之前运行。setUpClass作为唯一的参数被调用时,必须使用classmethod()作为装饰器
        '''    
        print("start and init")
        cls.a=1111


    @classmethod
    def tearDownClass(cls):
        '''
        一个类方法在单个类测试之后运行。setUpClass作为唯一的参数被调用时,必须使用classmethod()作为装饰器

        '''
        print("end and clear")


if __name__ == "__main__":
    unittest.main()



    '''
    TestCase    实例为一个测试用例
    TestSuite   多个测试用例的集合，TestSuite也可以嵌套TestSuite。
    TestRunner  执行测试用例
    TestLoader  加载TestCase到TestSuite中的
    TestFixture 对一个测试用例环境的搭建和销毁，是一个fixture, TestCase的setUp()和tearDown()方法来实现

    '''
