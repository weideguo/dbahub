# 使用python实现map reduce示例


```shell
#创建样本文件
#cd /tmp/test
cat > /tmp/test/sample.txt <<EOF
2011 20
2011 10
2011 34
2011 19
2011 20
1011 50
2011 30
2011 27
2011 15
EOF


##创建文件可执行文件 map_demo.py reduce_demo.py
chmod 755 *py


#上传文件到hdfs
hadoop fs -put -f /tmp/test /tmp/test


#运行mapreduce任务
hadoop jar $HADOOP_HOME/jars/hadoop*streaming*.jar \
-input /tmp/test/sample.txt \
--output /test/output \
--mapper /tmp/test/map_demo.py \
--reducer /tmp/test/reduce_demo.py \
--file /tmp/test/map_demo.py \
--file /tmp/test/reduce_demo.py


#查看结果
hadoop fs -cat /test/output/*


#删除结果集
hadoop fs -rm -f -r /test/output/*


```


