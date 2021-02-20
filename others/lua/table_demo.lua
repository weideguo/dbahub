
-- 普通的table
t={}
t.a="aaaa"
print(t.a)

function t.f(x)
    print(x)
end

t.f('aaaaa')


-- metatable

mytable = {}                 -- 普通表
t = {}                       -- 元表 
setmetatable(mytable, t)     -- 把 t 设为 mytable 的元表   通过此获取的表可以设置两个表的操作，如相加

getmetatable(mytable)        -- 返回mytable 的元表


other = { foo = 3 }
t = setmetatable({}, { __index = other })
t.foo


-- 元方法
-- __index 访问元素不存在时，调用该函数处理
mytable = setmetatable({key1 = "value1"}, {
  __index = function(mytable, key)
    if key == "key2" then
      return "metatablevalue"
    else
      return nil
    end
  end
})

print(mytable.key1, mytable.key2)

-- __newindex = function(mytable, key, value)        __newindex 新创建的索引已经存在则赋值，不存在则调用该方法

-- __add = function(mytable, newtable)               mytable + newtable 调用

-- __call = function(mytable, newtable)              mytable(newtable)调用

-- __tostring = function(mytable)                    print()调用的方法




t = { "aaa", "bbb", "ccc" }
for k,v in ipairs(t) do
    print(k,v)
end


a={}
next(a)   --判断是否为空 
a=={}     --不能用此判断


-- pairs(t)
