# 这是一个非常简单的mysql udf实现demo

## 1.编译cpp文件
<em>假设mysql的头文件目录是/u01/mysql5631/include </em>

>`g++ -shared -fPIC -I /u01/mysql5631/include -o test_add.so test_add.cpp`

## 2.将编译好的so文件复制到mysql的plugin目录下

>`cp test_add.so /u01/mysql5631/lib/plugin`

## 3.在mysql中创建function

>mysql> `CREATE FUNCTION testadd RETURNS INTEGER SONAME 'test_add.so'`

## 4.使用function

>mysql> `select  testadd(1,4);`<br /> 
>+--------------+ <br /> 
>| testadd(1,4) | <br /> 
>+--------------+ <br /> 
>|  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;          5 | <br /> 
>+--------------+

>select * from mysql.func;

