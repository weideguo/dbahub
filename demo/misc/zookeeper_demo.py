#coding:utf8
#预先条件
#1.安装zookeeper的c客户端
#2.安装python的zkpython包
#3.设置export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib 用于指定libzookeeper_mt.so.2.0.0


import zookeeper

zk=zookeeper.init("127.0.0.1:2181")

zookeeper.get_children(zk,'/zookeeper',None)  #获取节点下的子节点

zookeeper.get(zk,'/zookeeper/quota')
zookeeper.get(zk,'/zookeeper/quota',None)
zookeeper.set(zk,'/weideguo','yyyyy') 

#需要权限控制？？
#zookeeper.create(zk,'/weideguo','{"name":"wei"}',0)
