
require("module")

print(module.constant)
module.func3()



x =  require("module")

print(x.constant)
x.func3()

--[[

通过相对路径引入（相对于启动lua时的目录，不是相对于当前lua文件的）
x=require("path_to_lua_lib/module")

require 用于搜索 Lua 文件的路径是存放在全局变量 package.path 中
当 Lua 启动后，会以环境变量 LUA_PATH 的值来初始这个环境变量

export LUA_PATH=path_to_lua_lib

打印加载lua的目录，以“;”分隔
print(package.path)



#调用动态连接库
local path = "/usr/local/lua/lib/libluasocket.so"
-- path = "C:\\windows\\luasocket.dll"      --这是 Window 下
local f = loadlib(path, "luaopen_socket")

--]]