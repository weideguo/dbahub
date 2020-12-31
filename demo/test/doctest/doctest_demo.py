#coding:utf8                                              
"""
doctest用例
'>>>' 开头的行就是doctest测试用例。
不带 '>>>' 的行就是测试用例的输出。输出后不要带有多余的空格。
如果实际运行的结果与期望的结果不一致，就标记为测试失败。
运行
python unnecessary_math.py
#没有 __main__ 模块时运行
python -m doctest unnecessary_math.py 
python -m doctest -v unnecessary_math.py 
"""
def multiply(a, b):
    """
    >>> multiply(4, 3)
    12
    >>> multiply('a', 3)
    'aaa'
    """
    return a * b

#if __name__=='__main__':
#    import doctest
#    doctest.testmod(verbose=False)                 