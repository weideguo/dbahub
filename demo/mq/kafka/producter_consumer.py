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

通过 group_id 实现一条消息是否可以被多个消费者消费？
"""
consumer = KafkaConsumer(topic, bootstrap_servers=addrs)

#由kafka push
for msg in consumer:
    #(msg.topic, msg.partition, msg.offset, msg.key, msg.value)
    print(msg)
    
    
while True:
    msg = consumer.poll(timeout_ms=5)    # 从kafka获取消息  没有数据，则拉取到的为空 
    
 
 
###################################################################################

#生产者设置序列化 则可以直接 send json格式的数据
producer = KafkaProducer( value_serializer=lambda m: json.dumps(m).encode('ascii'))

#消费者设置反序列化 则可以获取到json格式的数据
consumer = KafkaConsumer( value_deserializer=lambda m: json.loads(m.decode('ascii')))


#消费者订阅多个topic
consumer = KafkaConsumer()
consumer.subscribe(pattern= '^topic*')               #使用正则列出订阅的topic
consumer.subscribe(topics= ['topic_0', 'topic_1'])   #



 
    