
co = coroutine.create(function(a,b)
    print("resume args:"..a..","..b)
    yreturn = coroutine.yield()
    print("yreturn :"..yreturn)
end)

a,b=coroutine.resume(co,0,1)                     --首次执行协程co时，参数传递给协程co的函数，函数运行到yield
print(a,b)
c=coroutine.resume(co,2100)                     --再次执行协程co时，参数会作为给协程中上一次yeild的返回值
print(c)

-- 判断协程的状态
coroutine.status(co)



-----------------------------------------------------

co2 = coroutine.wrap(function (a,b)
    print("resume args:"..a..","..b)
    yreturn = coroutine.yield(a,b)           -- yield内的返回给第一次传入，=左边的为第二次传入参数
    print ("yreturn :"..yreturn)
end)

print(type(co2))           --coroutine.create创建的为thread

a,b=co2(0,1)               -- yield内的返回给第一次传入
print(a, b)
c=co2(21)                  -- =左边的为第二次传入参数，没有返回值
print(c)


-----------------------------------------------------

function foo(a)
    print("foo", a)
    return coroutine.yield(2 * a)
end

co = coroutine.create(function ( a, b )
    print("co-body", a, b)
    local r = foo(a + 1)
    print("co-body", r)
    local r, s = coroutine.yield(a + b, a - b)
    print("co-body", r, s)
    return b, "end"
end)

print("main", coroutine.resume(co, 1, 10))
print("main", coroutine.resume(co, "r"))
print("main", coroutine.resume(co, "x", "y"))
print("main", coroutine.resume(co, "x", "y"))


