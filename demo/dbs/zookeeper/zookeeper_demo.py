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

"""
zookeeper.create(self.handle, path, data, [acl2], flags)

zookeeper.create(zk,'/weideguo','{"name":"wei"}',[{"perms":0x1f,"scheme":"world","id":"anyone"}],0);

ACL
int READ = 1 << 0;
int WRITE = 1 << 1;
int CREATE = 1 << 2;
int DELETE = 1 << 3;
int ADMIN = 1 << 4;

flags
过期的时间

"""