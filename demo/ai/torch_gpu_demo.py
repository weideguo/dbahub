"""
pip install torch
"""
import torch

# 查看cuda是否可用
torch.cuda.is_available()

# 当前GPU设备
torch.cuda.current_device()

# 查看GPU
torch.cuda.device_count()

# i为 device_count() 的range编号
device = torch.device(f'cuda:{i}')

# 使用cpu
#device = torch.device('cpu')

# 设置张量存储在GPU上
torch.ones(2, 3, device=device)


# 神经网络
from torch import nn
net = nn.Sequential(nn.Linear(3, 1))
net = net.to(device=device)



