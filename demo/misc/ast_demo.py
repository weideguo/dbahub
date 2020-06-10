#coding:utf8
Num = lambda env, n: n
Var = lambda env, x: env[x]
Add = lambda env, a, b:_eval(env, a) + _eval(env, b)
Mul = lambda env, a, b:_eval(env, a) * _eval(env, b)
 
_eval = lambda env, expr:expr[0](env, *expr[1:])
 
env = {'a':2, 'b':5}
tree = (Add, (Var, 'a'),
             (Mul, (Num, 3),
                   (Var, 'b')))
 
print(_eval(env, tree))

"""
抽象语法树 Abstract Syntax Trees
计算
a + 3 * b
"""
"""

_eval(env, tree)
= _eval({'a':2, 'b':5}, (Add, (Var, 'a'), (Mul, (Num, 3),
                                               (Var, 'b'))) )
           
= Add({'a':2, 'b':5}, (Var, 'a'), (Mul, (Num, 3),
                                        (Var, 'b')) )



= _eval({'a':2, 'b':5}, (Var, 'a')) + _eval({'a':2, 'b':5}, (Mul, (Num, 3),
                                                                  (Var, 'b')) )


_eval({'a':2, 'b':5},(Var, 'a'))
= Var({'a':2, 'b':5},'a')
= {'a':2, 'b':5}['a']

"""


