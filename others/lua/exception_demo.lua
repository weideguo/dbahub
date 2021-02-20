--错误处理

function f1(a,b)
   assert(type(a) == "number", "a 不是一个数字")
   assert(type(b) == "number", "b 不是一个数字")      --判断表达式为false时则发错报错信息
   return a+b
end

f1(10)


--------------------------------------

function f(i) 
    print(i) 
    error("error..")              --发出报错信息
    print("xxxx")
end

pcall(f, 33);print("xxxxx")       --调用的函数遇到错误则退出，但不会有报错信息，不影响之后的操作
f(33);print("xxxxx")              --调用的函数遇到错误则退出，有报错信息，之后的操作会被中止

--[[
if pcall(function_name, ….) then
-- no error
else
-- some error
end
--]]
--------------------------------------


function myfunction(a)
   n = n/4
   --print(a)
end

function myerrorhandler( err )
   print( "ERROR:", err )
end

status = xpcall( myfunction, myerrorhandler )
print( status)






