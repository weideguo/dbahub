modulex = {}
 

modulex.constant = "这是一个常量"
 

function modulex.func1()
    io.write("这是一个公有函数！\n")
end
 
local function func2()
    print("这是一个私有函数！")
end
 
function modulex.func3()
    func2()
end
 
return modulex
