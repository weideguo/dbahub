"""
模型的存储、加载
"""

"""
只保存模型参数，不保存模型结构。加载时先创建模型实例。
"""
torch.save(model.state_dict(), 'model_weights.pth')



model = MyModel()                                         # 模型实例化
model.load_state_dict(torch.load('model_weights.pth'))
model.eval()                                              # 评估模式
"""
model.train()   
默认为训练模式
按概率随机丢弃神经元，启用梯度计算
"""




"""
保存模型结构+参数。但可能在不同PyTorch版本间不兼容。不推荐。
"""

torch.save(model, 'full_model.pth')

# 加载模型（依旧需要预先定义模型类，只是不需要实例化）
model = torch.load('full_model.pth',weights_only=False)
model.eval()




"""
保存训练状态，包括优化器、epoch等信息，便于恢复训练。
"""

# 保存检查点
checkpoint = {
    'epoch': epoch,                                          
    'model_state_dict': model.state_dict(),
    'optimizer_state_dict': optimizer.state_dict(),
    'loss': loss,
}
torch.save(checkpoint, 'checkpoint.pth')

# 加载检查点
checkpoint = torch.load('checkpoint.pth')
model.load_state_dict(checkpoint['model_state_dict'])
optimizer.load_state_dict(checkpoint['optimizer_state_dict'])
epoch = checkpoint['epoch']
loss = checkpoint['loss']


"""
ONNX格式，跨框架通用
Open Neural Network Exchange

"""



"""
# safetensors 文件
# 张量存储文件格式
pip install safetensors
"""

"""
保存模型权重
"""
from safetensors.torch import save_file

state_dict = model.state_dict()
save_file(state_dict, "model.safetensors")


# 加载模型
from safetensors.torch import load_file

model = MyModel()                       
state_dict = load_file("model.safetensors")           
#state_dict = load_file("model.safetensors", device="cuda")
model.load_state_dict(state_dict)
model.eval()


