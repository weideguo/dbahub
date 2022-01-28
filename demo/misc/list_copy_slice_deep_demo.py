#浅拷贝(slice cpoy)		对原对象修改影响其他				
#元素只是引用
person=['name',['savings',100]]

#对savings 或者100修改都影响 person hubby wify
hubby=person[:]							#切片操作  [1:5]切取下标1个到5-1的元素;不指定则为全;  [::3] 元素间隔为3
wify=list(person)
hubby=person

"""
切片
[start:stop:step]

step 为负数，则为倒序
-1   间隔一个元素倒序，即没有元素减少
-2   间隔两个元素倒序，即每隔离一个元素取一个
1    间隔一个元素，即没有元素减少
2    间隔两个元素，即每隔离一个元素取一个
"""
#####################################
#深拷贝(deep copy) 对原对象修改不影响其他

import copy
wify=copy.deepcopy(person)