# pip install chromadb

import chromadb



chroma_client = chromadb.Client()

"""
# 本地持久化模式
chroma_client = chromadb.PersistentClient(path="/path/to/data")
"""

"""
# 服务器模式
chroma_client = chromadb.HttpClient(host="localhost", port=8000)
"""


collection = chroma_client.create_collection(name="my_collection")

"""
chroma_client.list_collections()
chroma_client.delete_collection(name="my_collection")
collection = client.get_collection("testname")
collection.count()
"""




# 增加或者更新
collection.upsert(
    ids=["id1"],
    embeddings=[[1.1, 2.2, 3.3]],
    metadatas=[{"chapter": "3", "verse": "16"}],
    documents=["这是一个文档的内容"],
)


"""
collection.add()     # 插入数据
collection.get()     # 获取collection的所有item
collection.peek()    # 看看5个
"""


# 查询
collection.query(
    query_embeddings=[[1.1, 2.3, 3.2], [5.3, 4.2, 2.1]],
    n_results=2,
    where={"chapter": "3"}
)

results = collection.query(
  query_texts=["Document"],
  n_results=2
)


# 删除
collection.delete(ids=["uri1"])

