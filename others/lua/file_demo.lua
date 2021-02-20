-- 以只读方式打开文件
file = io.open("/tmp/test.txt", "r")
io.input(file)
print(io.read())
io.close(file)


-- 以附加的方式打开只写文件
file = io.open("/tmp/test.txt", "a")
io.output(file)
io.write("hello\n")
io.close(file)

--[[
io.read                                                    
"*n"	读取一个数字并返回它。                                file.read("*n")
"*a"	从当前位置读取整个文件。                              file.read("*a")
"*l"    默认，读取下一行，在文件尾 (EOF) 处返回 nil。         file.read("*l")
number	返回一个指定字符个数的字符串，或在 EOF 时返回 nil。   file.read(5)
--]]


--[[
io.open 模式
r	以只读方式打开文件，该文件必须存在。
w	打开只写文件，若文件存在则文件长度清为0，即该文件内容会消失。若文件不存在则建立该文件。
a	以附加的方式打开只写文件。若文件不存在，则会建立该文件，如果文件存在，写入的数据会被加到文件尾，即文件原先的内容会被保留。（EOF符保留）
r+	以可读写方式打开文件，该文件必须存在。
w+	打开可读写文件，若文件存在则文件长度清为零，即该文件内容会消失。若文件不存在则建立该文件。
a+	与a类似，但此文件可读可写
b	二进制模式，如果文件是二进制文件，可以加上b
+	号表示对文件既可以读也可以写
--]]


-- 以只读方式打开文件
file = io.open("/tmp/test.txt", "r")
print(file:read())
file:close()

-- 以附加的方式打开只写文件
file = io.open("/tmp/test.txt", "a")
file:write("hello\n")
--file:flush()
file:close()

