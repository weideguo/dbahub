#coding:utf-8
#pip install sqlparse

import sqlparse


raw = 'select * from foo; select * from bar;'

statements = sqlparse.split(raw)
#['select * from foo;', 'select * from bar;']  分割成单独的语句


#格式化
format_sql=sqlparse.format(statements[0], reindent=True, keyword_case='upper')


#解析
parsed=sqlparse.parse(statements[0])[0]
parsed.tokens

parsed.get_type()

