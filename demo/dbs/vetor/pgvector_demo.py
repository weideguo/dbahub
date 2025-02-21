
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

# !/usr/bin/env python3
from text2vec import SentenceModel
from psycopg2 import connect


# 需要从huggingface下载模型保存在当前目录
model = SentenceModel("shibing624/text2vec-base-chinese")


def query(question, limit=64):
    vec = model.encode(question)  # 由输出的问题生成向量
    item = "ARRAY[" + ",".join([str(f) for f in vec.tolist()]) + "]::VECTOR(768)"

    # 连接到pgvector
    cursor = connect("host=xxx dbname=xxx user=xxx password=xxx port=xxx").cursor()

    # 使用向量在数据库中查找
    cursor.execute("""SELECT id, txt, vec <-> %s AS d FROM sentences ORDER BY 3 LIMIT %s;""" % (item, limit))
    
    for id, txt, distance in cursor.fetchall():
        print("%-6d [%.3f]\t%s" % (id, distance, txt))


query("实际的问题",8)

