
"""
-- https://git.postgresql.org/gitweb/?p=pgrpms.git;a=commit;h=061d9fd2a1f408157094117378bd6c8f3c78bb95
-- 安装pgvector
CREATE EXTENSION vector;
CREATE TABLE sentences
(

    id    BIGINT PRIMARY KEY,  -- 标识

    txt   TEXT NOT NULL,       -- 文本

    vec   VECTOR(768) NOT NULL -- 向量

);

-- 数据清洗灌入
"""

"""
OpenAI 提供了将自然语言文本转换为数学向量的 API ：
例如 text-embedding-ada-002 ，便可以将最长2048～8192个字符的句子/文档转换为一个 1536 维的向量。
这里选择使用 HuggingFace 上的 shibing624/text2vec-base-chinese 模型替代完成文本到向量的转换。编码为 768 维的向量。
"""

# !/usr/bin/env python3

from text2vec import SentenceModel

from psycopg2 import connect

model = SentenceModel('shibing624/text2vec-base-chinese')


def query(question, limit=64):

    vec = model.encode(question)  # 生成一个一次性的编码向量，默认查找最接近的64条记录

    item = 'ARRAY[' + ','.join([str(f) for f in vec.tolist()]) + ']::VECTOR(768)'

    # 连接到pgvector
    cursor = connect('postgres:///').cursor()

    # 向量最近邻搜索
    cursor.execute("""SELECT id, txt, vec <-> %s AS d FROM sentences ORDER BY 3 LIMIT %s;""" % (item, limit))
    
    for id, txt, distance in cursor.fetchall():

        print("%-6d [%.3f]\t%s" % (id, distance, txt))



query("实际的问题",8)

