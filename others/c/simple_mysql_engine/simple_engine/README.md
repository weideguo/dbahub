
``` shell
#g++ -std=c++11 -shared -fPIC \
#-I /usr/include/mysql/ \
#-I /usr/include/mysql/private  \
#-L /usr/lib64 \
#-o ha_minimal.so ha_minimal.cc  


# 需要先下载 boost_1_59_0
# 需要先运行cmake生成必要的.h文件
cmake . -DCMAKE_INSTALL_PREFIX=/data/mysql5744 \
        -DWITH_BOOST=/data/boost_1_59_0         


g++ -std=c++11 -shared -fPIC \
-I /data/mysql-5.7.44/mysql-5.7.40/include/      \
-I /data/mysql-5.7.44/mysql-5.7.40/libbinlogevents/export \
-I /data/mysql-5.7.44/mysql-5.7.40/sql  \
-DMYSQL_DYNAMIC_PLUGIN  \
-L /data/mysql5744/lib \
-o ha_minimal.so ha_minimal.cc  
 

编译成功，但安装插件失败？
```
