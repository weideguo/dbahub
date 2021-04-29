import tempfile

fp = tempfile.TemporaryFile()            #创建临时文件 调用关闭方法后自动删除文件
fp.write(b'Hello world!')
fp.name
fp.seek(0)
fp.read()
fp.close()

tmpdir=tempfile.TemporaryDirectory()     #创建临时目录于/tmp目录下，删除对象之后自动删除目录
del tmpdir



tempfile.NamedTemporaryFile()            #跟TemporaryFile类似，但在/tmp目录下显式生产文件


f=tempfile.SpooledTemporaryFile()        #跟TemporaryFile类似，但只在内存中直到达到max_size
f.rollover()                             #手动刷新到磁盘 

