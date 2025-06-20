"""
transformers 实现推理
"""

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, GenerationConfig

# 模型路径
mode_name_or_path = './deepseek-ai/deepseek-llm-7b-chat'

# 分词器
tokenizer = AutoTokenizer.from_pretrained(mode_name_or_path, trust_remote_code=True)
# 模型
model = AutoModelForCausalLM.from_pretrained(mode_name_or_path, trust_remote_code=True,torch_dtype=torch.bfloat16,  device_map="auto")
model.generation_config = GenerationConfig.from_pretrained(mode_name_or_path)
model.generation_config.pad_token_id = model.generation_config.eos_token_id
# 设置模型为评估模式
model.eval()


prompt = "实际向大模型提问的问句"

messages = [
    {"role": "user", "content": prompt}
]

# 构建输入     
input_tensor = tokenizer.apply_chat_template(messages, add_generation_prompt=True, return_tensors="pt")
# 通过模型获得输出
max_length = 10*1024*1024   # 请求最大长度
outputs = model.generate(input_tensor.to(model.device), max_new_tokens=max_length)
result = tokenizer.decode(outputs[0][input_tensor.shape[1]:], skip_special_tokens=True)


