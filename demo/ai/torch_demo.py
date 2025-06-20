import torch
import torch.nn as nn
import torch.optim as optim


# 创建一些随机数据作为示例
x_train = torch.randn(100, 1)                        # 100个样本，每个样本1个特征
y_train = 2 * x_train + 1 + 0.1*torch.randn(100, 1)  # 线性关系 y = 2x + 1，加上一些噪声
 
# 创建数据集和数据加载器
train_dataset = torch.utils.data.TensorDataset(x_train, y_train)
train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=10, shuffle=True)


class LinearModel(nn.Module):
    def __init__(self):
        super(LinearModel, self).__init__()
        self.linear = nn.Linear(1, 1)  # 一个输入特征和一个输出特征，x为输入，y为输出
    
    def forward(self, x):
        return self.linear(x)



model = LinearModel()
criterion = nn.MSELoss()                             # 使用均方误差作为损失函数
optimizer = optim.SGD(model.parameters(), lr=0.01)   # 使用随机梯度下降优化器

########## 训练模型
epochs = 100  # 训练轮数
for epoch in range(epochs):
    for inputs, targets in train_loader:
        # 前向传播
        outputs = model(inputs)
        loss = criterion(outputs, targets)
        
        # 后向传播和优化
        optimizer.zero_grad()  # 清空梯度
        loss.backward()        # 反向传播计算梯度
        optimizer.step()       # 根据梯度更新参数
    
    if (epoch+1) % 10 == 0:
        print(f'Epoch [{epoch+1}/{epochs}], Loss: {loss.item():.4f}')
        
        
        

########## 测试模型
x_test = torch.randn(10, 1)                   # 10个测试样本，每个样本1个特征
test_inputs = torch.unsqueeze(x_test, dim=1)  
predicted = model(test_inputs)                # 使用模型进行预测，即模型能用于计算 y = 2x + 1 ，x为输入，y为输出
print("Predicted values:", predicted)


# y_test = 2 * x_test + 1 + 0.1*torch.randn(10, 1)  
# 可以用 y_test 与 predicted 对比，评估模型的准确性

"""
损失函数
用于衡量 output 与 target 的差值

nn.L1Loss                      L1范数损失
nn.MSELoss                     均方误差损失
nn.CrossEntropyLoss            交叉熵损失 
nn.KLDivLoss                   散度损失
nn.BCELoss                     二进制交叉熵损失
nn.BCEWithLogitsLoss           
nn.MarginRankingLoss           
nn.HingeEmbeddingLoss          
nn.MultiLabelMarginLoss        
nn.SmoothL1Loss                平滑版L1损失
nn.SoftMarginLoss   
nn.MultiLabelSoftMarginLoss 
n.CosineEmbeddingLoss          cosine 损失
nn.MultiMarginLoss             多类别分类的hinge损失
nn.TripletMarginLoss           三元组损失
nn.CTCLoss                     连接时序分类损失
nn.NLLLoss                     负对数似然损失
nn.NLLLoss2d
nn.PoissonNLLLoss  


优化器
负责根据损失函数的梯度自动更新模型的参数（权重和偏置），使损失函数最小化。

optim.SGD()           基础随机梯度下降，可加动量（Momentum）        简单任务，需精细调参时
optim.Adam()          自适应学习率 + 动量，默认首选                 大多数深度学习任务（CNN/RNN）
optim.RMSprop()       自适应学习率（按梯度平方根缩放）              RNN/LSTM 等序列模型
optim.Adagrad()       为稀疏特征分配更大学习率                      稀疏数据、自然语言处理
optim.AdamW()         Adam + 权重衰减修正（解决 L2 正则化问题）     训练 Transformer 类模型
L-BFGS                二阶优化方法，收敛快但内存消耗大              小批量数据 + 高精度优化需求


将多元函数想象为山地地形图：
梯度方向 登山时最陡的上坡方向
梯度模长 山坡的陡峭程度
梯度为零 山顶（极大值）、山谷（极小值）或马鞍点
"""

