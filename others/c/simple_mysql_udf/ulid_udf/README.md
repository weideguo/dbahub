
``` shell
git clone https://github.com/suyash/ulid
# /usr/include/mysql 为mysql头文件所在位置，根据实际位置修改
g++ -std=c++11 -shared -fPIC -I /usr/include/mysql -o ulid_udf.so ulid_udf.cc
# /data/mariadb1039/lib/plugin/ 为mysql的plugin目录，据实际位置修改
cp ulid_udf.so /data/mariadb1039/lib/plugin/
```

``` sql
CREATE FUNCTION ulid RETURNS STRING SONAME "ulid_udf.so";

select hex(ulid());
```
