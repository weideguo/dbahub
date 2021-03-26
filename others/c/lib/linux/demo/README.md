
# 链接库编译
gcc func.c -shared -fPIC -o libfunc.so


# 主函数编译 只需要安装编译后的连接库以及头文件
gcc call_func.c -L./lib -lfunc -I ./include -o call_func


# 运行 只需要链接库
export LD_LIBRARY_PATH=./lib
./call_func


