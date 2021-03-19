#coding:uttf8

#发布者发送到topic的消息，只有订阅了topic的订阅者才会收到消息。


#生产者
from kafka import KafkaProducer

addr=["192.168.0.1:9092"]
producer = KafkaProducer(bootstrap_servers=addr)  

msg = "Hello World"                      
topic = "test"
producer.send(topic, msg.encode('utf-8'))  
producer.close()




###################################################################################

#消费者
from kafka import KafkaConsumer

addrs=['192.168.0.1:9092']
topic="test"

"""
group_id (str or None): The name of the consumer group to join for dynamic
    partition assignment (if enabled), and to use for fetching and
    committing offsets. If None, auto-partition assignment (via
    group coordinator) and offset commits are disabled.
    Default: None

相同 group_id 一条消息只消费一次
"""
consumer = KafkaConsumer(topic, bootstrap_servers=addrs)
#consumer = KafkaConsumer(topic, bootstrap_servers=addrs, group_id="test_group_1")

#由kafka push
for msg in consumer:
    #(msg.topic, msg.partition, msg.offset, msg.key, msg.value)
    print(msg)
    
    
while True:
    msg = consumer.poll(timeout_ms=5)    # 从kafka获取消息  没有数据，则拉取到的为空 
    
 
from kafka.structs import TopicPartition

consumer.partitions_for_topic(topic)                           # 获取主题的分区信息
consumer.topics()                                              # 获取主题列表                                                          
consumer.subscription()                                        # 获取当前消费者订阅的主题                                                            
consumer.assignment()                                          # 获取当前消费者topic、分区信息


##恢复
consumer.poll()                                                # 先进行一次假的拉取 以实现分配partition 
consumer.assignment()                                          # 查看分配的partition，只能设置分配的partition的offset；分配多个partition时，只需要设置一个partition的offset 
consumer.seek(TopicPartition(topic=topic, partition=0), 1)     # 重置偏移量，从第1个偏移量消费，包含设置的值，不设置默认从最新开始消费
consumer.position(TopicPartition(topic=topic, partition=0))    # 获取当前主题的最新偏移量 
 
consumer.seek_to_end()                                         
consumer.seek_to_beginning()
 
 
 
"""
#相同group_id情况下：
#客户端程序退出时，其分配的partition会被分配给其他还活着的客户端。客户端可以动态加入与退出，partition会自适应分配。启动客户端数大于partition时，只有已经分配partition的获取到数据，即获取数据的客户端数等于partition数。
#只有全部客户端都发生退出时才需要在启动客户端时设置恢复策略。
#客户端程序通过记录退出时的offset，从而实现定点恢复。  
#比如使用zookeeper共享退出时的offset。
#一个partition记录一个，恢复时只有匹配的partition的客户端设置offset，客户端匹配多个partition只需要设置timestamp最大值对于的offset。

partition=0, offset=1880021, timestamp=1615978811793
partition=1, offset=1934114, timestamp=1615978811078
partition=2, offset=1986215, timestamp=1615977759813
"""
 
 
###################################################################################

#生产者设置序列化 则可以直接 send json格式的数据
producer = KafkaProducer( value_serializer=lambda m: json.dumps(m).encode('ascii'))

#消费者设置反序列化 则可以获取到json格式的数据
consumer = KafkaConsumer( value_deserializer=lambda m: json.loads(m.decode('ascii')))


#消费者订阅多个topic
consumer = KafkaConsumer()
consumer.subscribe(pattern= '^topic*')               #使用正则列出订阅的topic
consumer.subscribe(topics= ['topic_0', 'topic_1'])   #



 
    