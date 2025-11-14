# 命令行表格展示

from tabulate import tabulate


data = [
{"Name","Age","City"},
{"N11","A1","C111"},
{"N222","A11","C2"},
]

headers = data[0]
rows = data[1:]


print(tabulate(rows, headers=headers, tablefmt="grid"))

"""
tablefmt
plain simple grid pipe orgtbl rst mediawiki latex 
"""
