from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int
    name: str = "origin"  

"""
自动实现
__init__ 
__repr__ 
__eq__
"""

p1 = Point(1, 2, "A")
print(p1) 

print(p1 == Point(1, 2, "A"))  
# True



class Point:
    def __init__(self,x,y,name="origin" ):
        self.x = x
        self.y = y
        self.name = name 






from dataclasses import dataclass, field

@dataclass
class Student:
    name: str = field(default_factory=str)
    grades: list[int] = field(default_factory=list)  


s = Student("AAA")
s.grades.append(111) 


s = Student()
s.name = "AAA"
s.grades.append(111) 



@dataclass
class Student:
    name: str
    grades: list[int] 

# 没有使用 field 自定义字段行为，则初始化必须带有所有字段
#s = Student()

"""
@dataclass
class Student:
    name: str = ''
    grades: list[int] = []   # 报错
"""
    


    
    