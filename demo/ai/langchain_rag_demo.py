"""
使用langchain实现RAG的简单示例

pip install langchain
pip install langchain-community
pip install langchain-openai
"""

from langchain.chains import RetrievalQA
from langchain.prompts import ChatPromptTemplate
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import TextLoader

# from langchain_core.documents import Document
# from langchain_core.embeddings import Embeddings


# 使用openai作为llm
# export OPENAI_API_KEY=
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
embeddings_model = OpenAIEmbeddings(model="text-embedding-ada-002")

"""
# 使用deepseek作为llm
# pip install langchain-deepseek
# export DEEPSEEK_API_KEY="your-api-key"

from langchain_deepseek import ChatDeepSeek

llm = ChatDeepSeek(
    model="...",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    # api_key="...",
    # other params...
)
"""

"""
from langchain_community.embeddings import HuggingFaceEmbeddings
# 需要先下模型到本地
embeddings_model = HuggingFaceEmbeddings(model_name="/path/2/m3e-base")
"""

# 数据导入向量数据库
# 加载文档，md、PDF、txt、doc
loader = TextLoader("/path/2/my.md", encoding="utf-8")
docs = loader.load()
# 将数据分块
text_splitter = RecursiveCharacterTextSplitter.from_language(language="markdown", chunk_size=200, chunk_overlap=0)
documents = text_splitter.create_documents(
    [docs[0].page_content]
)


# 使用向量数据库
# 需要先
db = FAISS.from_documents(documents, embeddings_model)
# 选择 top-2 相关的检索结果
retriever = db.as_retriever(search_kwargs={"k": 2})


# 自定义的提示词参数
# 创建带有 system 消息的模板
prompt_template = ChatPromptTemplate.from_messages([
    ("system", """你是一个XXX。

               已知信息:
               {context} """),
    ("user", "{question}")
])

chain_type_kwargs = {
    "prompt": prompt_template,
}


# RetrievalQA链
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",  # 使用stuff模式将上下文拼接到提示词中
    chain_type_kwargs=chain_type_kwargs,
    retriever=retriever
)

if __name__ == "__main__":
    user_question = "实际的问题"
    # 通过RAG链生成回答
    answer = qa_chain.run(user_question)
    print(answer)




