
> AST Abstract Syntax Tree 抽象的语法树
>
> 一些语法解析器
> Lex   Lexical Analyzar。
> Yacc  Yet Another Compiler Compiler。
> Bison 
> antlr


# antlr 
Another Tool for Language Recognition


词法分析器（Lexer）  
语法分析器（Parser）  
树分析器 （tree parser）  


antlr 主工程   主工程可以输入目标语言的语法描述grammer，生成对应运行时的parser。  
antlr 语法描述 grammer  
antlr 运行时 runtime  支持如Java，JavaScript，Python，C#  


#g4文件定义规则 grammer
### mysql
https://github.com/antlr/grammars-v4/blob/master/sql/mysql/Positive-Technologies/MySqlLexer.g4  
https://github.com/antlr/grammars-v4/blob/master/sql/mysql/Positive-Technologies/MySqlParser.g4  



mysql官方的文件解析存在冲突？type unicode object  
https://github.com/mysql/mysql-workbench/blob/8.0/library/parsers/grammars/MySQLLexer.g4  
https://github.com/mysql/mysql-workbench/blob/8.0/library/parsers/grammars/MySQLParser.g4  
https://github.com/mysql/mysql-workbench/blob/8.0/library/parsers/grammars/predefined.tokens  


### 其他语言
https://github.com/antlr/grammars-v4/


# 使用
```shell
##安装
cd /usr/local/lib
curl -O https://www.antlr.org/download/antlr-4.7.1-complete.jar
export CLASSPATH=".:/usr/local/lib/antlr-4.7.1-complete.jar:$CLASSPATH"
alias antlr4='java -Xmx500M -cp "/usr/local/lib/antlr-4.7.1-complete.jar:$CLASSPATH" org.antlr.v4.Tool'
alias grun='java org.antlr.v4.gui.TestRig'

#测试
java org.antlr.v4.Tool
#or
java -jar /usr/local/lib/antlr-4.7.1-complete.jar

#解析
antlr4 -Dlanguage=Python3 MySQLLexer.g4
antlr4 -Dlanguage=Python3 MySQLParser.g4

#产生python文件
#MyGrammarLexer.py
#MyGrammarParser.py
#MyGrammarListener.py (if you have not activated the -no-listener option)
#MyGrammarVisitor.py (if you have activated the -visitor option)


#安装运行时
pip install antlr4-python3-runtime
```



