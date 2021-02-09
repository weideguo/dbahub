#!/bin/bash


##重置位置参数 外部传入的值被覆盖
set -- v1 v2 v3     

echo $1     ##v1
echo $2     ##v2
echo $3     ##v3


set -- v11 v22 v33

echo $1
#使用shift可以移动位置参数
shift
echo $1
shift
echo $1
