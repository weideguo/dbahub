#
class Person(object):
  def __init__(self, name):
      self.name = name

  def get_first_name(self):
      return self.name.split()[0]

  def get_last_name(self):
      return self.name.split()[-1]
      
 p=Person("aaa bbb")     
      
#查看对象的属性 方法
dir(p)

#判断是否存在属性 方法
hasattr(jason, 'get_first_name')

#获取属性或方法
y=getattr(jason, 'name')
print y

x=getattr(jason, 'get_first_name')
x()
