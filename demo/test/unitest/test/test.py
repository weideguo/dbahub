#coding:utf8
import unittest
from src.math_func import *

class TestMathFunc(unittest.TestCase):
    #测试方法名需要以test开头
    #其他的命令格式会被忽略
    def test_add(self):
        self.assertEqual(3, add(1, 2))

    def test_minus(self):
        self.assertEqual(10, minus(20, 10))

    def test_multi(self):
        self.assertEqual(4, multi(2, 2))

    def test_divide(self):
        self.assertEqual(3, divide(7, 0))



   
def main():
    #默认全量运行测试
    #根据ACSII码的顺序加载测试用例，数字与字母的顺序为：0~9，A~Z，a~z 
    unittest.main(verbosity=2)


def main2():
    #'''
    suite = unittest.TestSuite()
    """
    只测试部分函数
    以及用于控制测试的顺序
    """
    suite.addTest(TestMathFunc("test_minus"))
    suite.addTest(TestMathFunc("test_add"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
    #'''


if __name__ == "__main__":
    main()
    #main2()


