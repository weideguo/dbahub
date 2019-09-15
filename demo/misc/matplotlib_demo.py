#coding:utf8
#linux下绘图 只需要进行一次操作
# cat ~/.config/matplotlib/matplotlibrc 
# backend : Agg
# import matplotlib as mpl  
# mpl.use('Agg')


import numpy as np
import matplotlib.pyplot as plt


plt.figure(2) # 创建图表1
ax1 = plt.subplot(211) # 在图表1中创建子图1
ax2 = plt.subplot(212) # 在图表1中创建子图2

x = np.linspace(0, 3, 100)
for i in range(5):
    plt.sca(ax1)   # 选择图表1的子图1
    plt.plot(x, np.sin(i*x))
    plt.sca(ax2)  # 选择图表1的子图2
    plt.plot(x, np.cos(i*x))

plt.show()
plt.savefig('/root/table.png')


for i in range(5):
    plt.figure(1)  # 选择图表2
    plt.plot(x, np.exp(i*x/3))

plt.show()
plt.savefig('/root/table2.png')
