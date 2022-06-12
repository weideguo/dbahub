#coding:utf8
import unittest

from unittest import TestCase
from unittest.mock import patch, Mock, ANY

import func_hub


class MyTest(TestCase):
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
     
    """
    patch 多个外部函数，那么调用遵循自下而上的规则
    @mock.patch("func_hub.abc2")
    @mock.patch("func_hub.abc1")
    def test_abc(self, mock_abc1, mock_abc2):
    
    patch(object, "function_name")   调用的只是一个函数 
    patch.object("function_name")    调用的只是一个类中的某个方法
    
    不在意它的内部实现而只是想调用这个函数然后得到结果而已，可以用 patch 方式来模拟
    """
     
    @patch("func_hub.abc")
    def test_abc(self, mock_abc):
        #构造一个返回结果
        mock_abc.return_value = "abc"
        
        #self.assertEqual(mock_abc(), "xxx")
        
        # 函数abc2要调用函数abc的结果，但函数abc由可能因为要连接外部服务等原因无法被正常调用，因此用mock模拟函数abc的返回，以确保函数abc2能够被正确测试
        #
        self.assertTrue(func_hub.abc2())
        
   
    @patch("func_hub.abc3")
    def test_abc2(self, mock_abc):
        mock_abc.return_value = "abc"                     # 构造函数返回
        mock_abc(a="aaa",b="bbb")                         # 构造函数的调用
        mock_abc.assert_called_once_with(a="aaa", b=ANY)  # 判断函数被调用的方式，即使传入的参数，ANY为全匹配
        
    def test_abc3(self):
        m = Mock(return_value="abc")                      # 构造一个虚假的函数，带有返回值
        m('foo', bar='baz')                               # 调用函数
        m.assert_called_once_with('foo', bar='baz')       # 判断函数的调用
        m('foo', bar='baz')                               # 再次调用函数
        #m.assert_called_once_with('foo', bar='baz')       # 再次判断函数的调用，不符合只调用一次因此测试不通过

if __name__ == "__main__":
    unittest.main()

"""
运行
python3 test_mock.py 


mock = Mock(return_value=None)
mock('foo', bar='baz')
mock.assert_called_once_with('foo', bar='baz')
mock('other', bar='values')
mock.assert_called_once_with('other', bar='values')
"""
