#coding:utf8
import sys
from antlr4 import *
"""
#将解析文件放在test目录下
cd ./test
antlr4 -Dlanguage=Python3 MySQLLexer.g4
antlr4 -Dlanguage=Python3 MySQLParser.g4
touch __init__.py
"""
from test.MySqlLexer import MySqlLexer as MyGrammarLexer
from test.MySqlParser import MySqlParser as MyGrammarParser
from test.MySqlParserListener import MySqlParserListener as MyGrammarListener


class CaseChangingStream():
    def __init__(self, stream, upper):
        self._stream = stream
        self._upper = upper

    def __getattr__(self, name):
        return self._stream.__getattribute__(name)

    def LA(self, offset):
        c = self._stream.LA(offset)
        if c <= 0:
            return c
        return ord(chr(c).upper() if self._upper else chr(c).lower())

 
def main(argv):
    input_stream = FileStream(argv[1],encoding="utf-8",errors="ignore")
    #sql gammer 可能只解析大写的，在此将原文件进行转换，除了处理关键字，不会影响其他数据的大小写分析
    upper_stream = CaseChangingStream(input_stream, True)
    lexer = MyGrammarLexer(upper_stream)
    stream = CommonTokenStream(lexer)
    parser = MyGrammarParser(stream)
    tree = parser.root()      #由MySqlParser.g4的第一条语法规则确定入口函数
 
    printer = KeyPrinter()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)
    print("---------------------------")

 
class KeyPrinter(MyGrammarListener):
    """
    实现Listener的空函数
    """
    def enterCreateIndex(self, ctx):
        print(ctx)
        print("enter index")

    def exitCreateIndex(self, ctx):
        #help(ctx)
        t=ctx.tableName()
        print(t.getText())
        #help(t.getText())
        print("exist index") 

    def enterColumnCreateTable(self, ctx):
        #help(ctx.tableOption(2))   #TableOptionCommentContext
        #help(ctx.tableOption(1))   #TableOptionCharsetContext
        #help(ctx.tableOption(0))   #TableOptionEngineContext
        #help(ctx) #partitionDefinitions createDefinitions tableOption
        t=ctx.tableName()
        print(t.getText())
        e=ctx.tableOption(0).engineName()
        print(e.getText())
        print(ctx.tableOption(2).getText())
        print("enter create table")


if __name__ == '__main__':
    main(sys.argv)


#运行
#python sql_parser.py my_test.sql
