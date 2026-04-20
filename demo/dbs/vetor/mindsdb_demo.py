
# 启动服务
# $ docker run --name mindsdb_container \
# -e OPENAI_API_KEY='your_key_here' -p 47334:47334 -p 47335:47335#

# 通过python连接服务
server = mindsdb_sdk.connect('http://127.0.0.1:47334')

# 创建知识库
kb_creation_query = server.query(f"""
CREATE KNOWLEDGE_BASE movies_kb
USING
    embedding_model = {{
       "provider": "openai",
       "model_name": "text-embedding-3-large"
    }},
    metadata_columns = ['genre', 'expanded_genres', 'rating'],
    content_columns = ['content'],
    id_column = 'movie_id';
""")
kb_creation_query.fetch()

# 需要预先设置files.movies，如通过csv导入
# 从files.movies插入数据到知识库
insert_query = server.query("""
    INSERT INTO movies_kb
    SELECT movie_id,
        genre,
        expanded_genres,
        rating,
        content
    FROM   files.movies
    WHERE rating >= 7.5
    USING
        track_column = movie_id
    """).fetch() 


def search_kb(question, limit=100):
    server.query(f"""
    SELECT * FROM movies_kb
    WHERE content = '{question}' limit {limit};
    """).fetch() 

question = "实际检索的提问"
# search_kb
relevant_chunks_df = search_kb(question, limit=100)

"""
通过将检索结果与提问格式化成文本格式，通过大模型进行最后格式话，实现RAG
"""
