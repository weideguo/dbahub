import mmap

"""
mmap是一种虚拟内存映射文件的方法，即将一个文件或者其它对象映射到进程的地址空间，
实现文件磁盘地址和进程虚拟地址空间中一段虚拟地址的一一对映关系。
用于大文件的读取优化
"""
filename=""
with open(filename, 'rb') as f:
    buf = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    
#读取
print(buf[:100])