-- 基础类
Shape = {area = 0}

function Shape:new (o,side)
  o = o or {}
  setmetatable(o, self)
  self.__index = self
  side = side or 0
  self.area = side*side;
  return o
end

function Shape:printArea ()
  print("area ",self.area)
end

-- myshape = Shape:new(nil,10)
-- myshape:printArea()



-- 继承
Rectangle = Shape:new()

function Rectangle:new (o,length,breadth)
  o = o or Shape:new(o)
  setmetatable(o, self)
  self.__index = self
  self.area = length * breadth
  return o
end

--[[
-- 如果重写则覆盖原有方法
function Rectangle:printArea ()
  print("area2 ",self.area)
end
--]]

myrectangle = Rectangle:new(nil,10,20)
myrectangle:printArea()
