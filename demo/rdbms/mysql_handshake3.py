#################普通请求与响应
#demo1
"""
CREATE TABLE `yyy` (
  `a` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1

select * from yyyy;
+------+
| y    |
+------+
|    1 |
|    2 |
|    3 |
+------+

##请求
\x13\x00\x00                                                         #消息长度       
\x00                                                                 #序号
\x03                                                                 #命令 标识当前请求消息的类型
select * from yyyy                                                   #sql



##普通响应                                                               
\x01\x00\x00\x01                                                     #恒定  Result Set Header 结构？
\x01                                                                 #字段数
$                                                                    #
\x00\x00\x02\x03                                                     #恒定  
def                                                                  #目录名称：在4.1及之后的版本中，该字段值为"def"
\x04                                                                 #数据库名称长度
test                                                                 #数据库名称（Length Coded String）
\x04                                                                 #
yyyy                                                                 #数据表名称（Length Coded String）
\x04                                                                 #
yyyy                                                                 #表原始名称（Length Coded String）
\x01                                                                 #
y                                                                    #列（字段）名称（Length Coded String）
\x01                                                                 #
y                                                                    #列（字段）原始名称（Length Coded String）
\x0c?\x00\x0b\x00\x00\x00\x03\x00\x00\x00\x00\x00\x05\x00\x00\x03    
\xfe\x00\x00"\x00                                                    #EOF+告警计数+状态标志位  1+2+2
\x02\x00\x00\x04\x01
1
\x02\x00\x00\x05\x01
2
\x02\x00\x00\x06\x01
3
\x05\x00\x00\x07
\xfe\x00\x00"\x00

"""


#客户端 发给 服务端 的请求
c='\x13\x00\x00\x00\x03select * from yyyy'


#服务端 发给 客户端  的响应                                                             
s='\x01\x00\x00\x01\x01$\x00\x00\x02\x03def\x04test\x04yyyy\x04yyyy\x01y\x01y\x0c?\x00\x0b\x00\x00\x00\x03\x00\x00\x00\x00\x00\x05\x00\x00\x03\xfe\x00\x00"\x00\x02\x00\x00\x04\x011\x02\x00\x00\x05\x012\x02\x00\x00\x06\x013\x05\x00\x00\x07\xfe\x00\x00"\x00'
   

#客户端发出quit
"""
\x01\x00\x00        #消息长度
\x00                #序号
\x01                #命令

"""


#demo2
"""
##################
CREATE TABLE `test1` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `orderId` int(11) NOT NULL,
  `extraInfo` varchar(10) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `orderId` (`orderId`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=latin1


select * from test.test1;
+----+---------+-----------+
| id | orderId | extraInfo |
+----+---------+-----------+
| 20 |       1 |           |
+----+---------+-----------+
'\x01\x00\x00\x01\x03(\x00\x00\x02\x03def\x04test\x05test1\x05test1\x02id\x02id\x0c?\x00\x0b\x00\x00\x00\x03\x03B\x00\x00\x002\x00\x00\x03\x03def\x04test\x05test1\x05test1\x07orderId\x07orderId\x0c?\x00\x0b\x00\x00\x00\x03\x05P\x00\x00\x006\x00\x00\x04\x03def\x04test\x05test1\x05test1\textraInfo\textraInfo\x0c!\x00\x1e\x00\x00\x00\xfd\x01\x10\x00\x00\x00\x05\x00\x00\x05\xfe\x00\x00"\x00\x06\x00\x00\x06\x0220\x011\x00\x05\x00\x00\x07\xfe\x00\x00"\x00'


##解析
\x01\x00\x00\x01
\x03
(
\x00\x00\x02\x03
def
\x04
test
\x05
test1
\x05
test1
\x02
id
\x02
id
\x0c?\x00\x0b\x00\x00\x00\x03\x03B\x00\x00\x002\x00\x00\x03\x03
def
\x04
test
\x05
test1
\x05
test1
\x07
orderId
\x07
orderId
\x0c?\x00\x0b\x00\x00\x00\x03\x05P\x00\x00\x006\x00\x00\x04\x03
def
\x04
test
\x05
test1
\x05
test1
\t
extraInfo
\t
extraInfo
\x0c!\x00\x1e\x00\x00\x00\xfd\x01\x10\x00\x00\x00\x05\x00\x00\x05
\xfe\x00\x00"\x00
\x06\x00\x00\x06\x02
20\x01
1\x00
\x05\x00\x00\x07
\xfe\x00\x00"\x00


"""




