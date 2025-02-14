# pip install -U pymilvus
from pymilvus import MilvusClient
import numpy as np

# Milvus Lite  本地模式
client = MilvusClient("milvus_demo.db")

"""
# 连接服务器
client = MilvusClient(
    uri='http://localhost:19530', 
    token="root:Milvus"
) 
"""


client.create_collection(
    collection_name="demo_collection",
    dimension=384,                           
)


# 构建数据
docs = [
    "Artificial intelligence was founded as an academic discipline in 1956.",
    "Alan Turing was the first person to conduct substantial research in AI.",
    "Born in Maida Vale, London, Turing was raised in southern England.",
]

vectors = [[ np.random.uniform(-1, 1) for _ in range(384) ] for _ in range(len(docs)) ]
data = [ {"id": i, "vector": vectors[i], "text": docs[i], "subject": "history"} for i in range(len(vectors)) ]


# 插入数据
res = client.insert(collection_name="demo_collection", data=data)


# 进行检索
query_vectors = embedding_fn.encode_queries(["Who is Alan Turing?", "What is AI?"])
res = client.search(
    collection_name="demo_collection",            # target collection
    data=query_vectors,                           # a list of one or more query vectors, supports batch
    limit=2,                                      # how many results to return (topK)
    output_fields=["vector", "text", "subject"],  # what fields to return
)

