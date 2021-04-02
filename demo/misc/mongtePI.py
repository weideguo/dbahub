#coding:utf8
#使用蒙特卡洛算法计算Π

import random


def montePI(n=100):
	s=0
	for i in range(n):
		x=random.random()
		y=random.random()
		if (x*x+y*y)<1 :
			s=s+1
	return 4.0*s/n


montePI()
