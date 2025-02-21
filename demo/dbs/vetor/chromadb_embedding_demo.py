# 使用自建的ollama服务进行embedding
import chromadb.utils.embedding_functions as embedding_functions
 
ollama_ef = embedding_functions.OllamaEmbeddingFunction(
    url="http://localhost:11434/api/embeddings",
    model_name="llama2",
)
 
embeddings = ollama_ef(["This is my first text to embed",
                        "This is my second document"])
                      

         
# 需要先从HuggingFace 下载模型 shibing624/text2vec-base-chinese
text2vec_ef = embedding_functions.text2vec_embedding_function(model_name = "shibing624/text2vec-base-chinese")



# 使用openai的api
openai_ef = embedding_functions.openai_embedding_function( model_name= "text-embedding-ada-002",
api_key="",
organization_id="",
api_base=""
)




