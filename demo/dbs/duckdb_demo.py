"""
无需安装服务端
pip install duckdb
"""

import duckdb
cursor = duckdb.connect()
# 创建文件逗号分隔文件test.csv，即可当成表查询 
print(cursor.execute("SELECT * FROM 'test.csv';").fetchall())

