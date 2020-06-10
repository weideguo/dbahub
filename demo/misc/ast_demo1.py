#coding:utf8

#源代码解析 --> 语法树 --> 抽象语法树(AST) --> 控制流程图 --> 字节码


func_def = """
def add(x, y):
    return x + y
print(add(3, 5))
"""


#compile编译得到字节码，cm即code对象
cm = compile(func_def, '<string>', 'exec')

#查看类型
import types
isinstance(cm, types.CodeType)

#执行字节码
exec(cm)
#执行string
#exec(func_def)

import ast
r_node = ast.parse(func_def)
#导出抽象语法树
ast.dump(r_node)

#更友好的展示
#pip install astunparse
import astunparse

print(astunparse.dump(r_node))
print(astunparse.unparse(r_node))



"""
class CodeVisitor(ast.NodeVisitor):
    pass

visitor = CodeVisitor()
visitor.visit(r_node)
"""

"""
父类
ast.NodeVisitor
继承函数
visit_
"""
class CodeTransformer(ast.NodeTransformer):
    def visit_BinOp(self, node):
        if isinstance(node.op, ast.Add):
            #函数方法替换
            node.op = ast.Sub()
        self.generic_visit(node)
        return node
    
    def visit_FunctionDef(self, node):
        self.generic_visit(node)
        #替换函数名
        if node.name == 'add':
            node.name = 'sub'
        #args_num = len(node.args.args)
        #args = tuple([arg.id for arg in node.args.args])
        func_log_stmt = "print('calling func')"
        #插入行
        node.body.insert(0, ast.parse(func_log_stmt))
        return node
    
    def visit_Name(self, node):
        replace = {'add': 'sub', 'x': 'a', 'y': 'b'}
        #参数名替换
        re_id = replace.get(node.id, None)
        node.id = re_id or node.id
        self.generic_visit(node)
        return node


transformer = CodeTransformer()
#修改语法树实现对字节码中函数的修改
n_node = transformer.visit(r_node)

#查看修改后的源码
source = astunparse.unparse(n_node)
print(source)

#运行修改后的源码
exec(compile(source, '<string>', 'exec'))
exec(compile(ast.parse(source), '<string>', 'exec'))



