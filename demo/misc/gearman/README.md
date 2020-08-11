#gearman 
分布式任务调度  
client 发出调度信息，woker执行后返回给client  
client通过任务名调度worker，当一个client调度多个woker，woker会自动轮询选择一个来执行  
woker挂掉会自动被剔除  


## install
```shell 
yum install gearmand  #安装
gearmand              #运行
```


## role
client： 提交任务    自行实现
server： 分配任务    gearman实现
worker： 执行任务    自行实现


## 部署样例 
可以选择一个或多个gearman server
```
      +---------+   +---------+   +---------+
      |  client |   |  client |   |  client |
      +----+----+   +---+-----+   +-----+---+
           |            |               |
           |            |               |
           +-----+------+---------+-----+
                 |                |
           +-----+-----+    +-----+-----+
           |           |    |           |
           |  server   |    |  server   |
           |           |    |           |
           +----+------+    +-------+---+
                |                   |
    +-----------+--+-------------+--+-----------+
    |              |             |              |
+---+-----+   +----+----+   +----+----+   +-----+---+
|  worker |   |  worker |   |  worker |   |  worker |
+---------+   +---------+   +---------+   +---------+
```
