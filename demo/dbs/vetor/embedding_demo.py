"""
# pip install sentence-transformers

sentence-transformers 提供了多种预训练模型，每种模型针对不同的应用场景进行了优化。

基础模型：
all-MiniLM-L6-v2           轻量级模型，适用于通用任务，快速且高效。
paraphrase-MiniLM-L6-v2    专为句子相似度和释义检测设计，精准匹配语义相近的句子。
multi-qa-MiniLM-L6-cos-v1  面向问答系统和信息检索，提升查询的准确性。
stsb-roberta-large         针对语义文本相似度（Semantic Textual Similarity，STS）任务进行了强化，适用于需要高精度相似度计算的场景。

其他预训练模型
https://www.sbert.net/docs/sentence_transformer/pretrained_models.html
"""



from sentence_transformers import SentenceTransformer

# 从目录中加载，如果模型不存在，则自动从huggingface下载模型
# git clone https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2   # 使用git下载
model = SentenceTransformer("all-MiniLM-L6-v2")   


sentences = ["我喜欢吃苹果", "我喜欢广州"]
embeddings = model.encode(sentences)

print(embeddings.shape) 



########################################## 计算相似度
from sentence_transformers import util
# 余弦相似度
cosine_sim = util.cos_sim(embeddings[0], embeddings[1])


sentences = ["猫在沙发上睡觉", "一只猫正在沙发上打盹"]
embedding1 = model.encode(sentences[0], convert_to_tensor=True)    # array -> tensor
embedding2 = model.encode(sentences[1], convert_to_tensor=True) 

similarity = model.similarity(embedding1, embedding2)              # 与util.cos_sim一样




######################################### 使用自己的数据集合训练
from sentence_transformers import SentenceTransformer, InputExample, losses
from torch.utils.data import DataLoader

# 自定义的训练数据，自己定义相似度
train_examples = [
    InputExample(texts=["样例句子1", "与样例句子1相似的句子"], label=1.0),
    InputExample(texts=["样例句子2", "与样例句子2不相似的句子"], label=0.0)
]
train_dataloader = DataLoader(train_examples, shuffle=True, batch_size=16)


model = SentenceTransformer("all-MiniLM-L6-v2")

# 定义损失函数
train_loss = losses.CosineSimilarityLoss(model)

# 微调模型
model.fit(train_objectives=[(train_dataloader, train_loss)], epochs=3)

# 保存成新模型
model.save("all-MiniLM-L6-v2-20250218")
