#coding:utf-8

#assert expression
assert 1==0
#等价于
#if not expression:
if not 1==0:
    raise AssertionError(arguments)


#可以加提示参数
#assert expression [, arguments]
import sys
assert ('linux' in sys.platform), "该代码只能在 Linux 下执行"


