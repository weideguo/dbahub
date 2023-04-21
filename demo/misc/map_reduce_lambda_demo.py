#-*-encoding:utf-8-*-

def f1(x):
	return x

def f2(x,y):
	return x+y
	
	
h=[10,11,12]
map_result=map(f1,h)      
reduce_result=reduce(f2,h)
print('map: '+str(map_result))
print('reduce '+str(reduce_result))

list(map_result)

f=lambda x,y,z:x*y*z
	
f(1,2,3)	##输出为1*2*3
