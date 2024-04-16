import pika


username = "guest"                                                                                    
pwd = "guest"
cred = pika.PlainCredentials(username, pwd)
#conn = pika.BlockingConnection(pika.ConnectionParameters("192.168.59.132", credentials=cred))   
conn = pika.BlockingConnection(pika.ConnectionParameters(host=["192.168.59.132:5672"], credentials=cred))   
channel = conn.channel()                                                                             


                    



# 直接交换机
channel.exchange_declare(exchange="direct_logs", exchange_type="direct")
 
severity = "error"
message = "This is an error message"
channel.basic_publish(exchange="direct_logs",routing_key=severity,body=message)
                      

# 广播交换机
channel.exchange_declare(exchange="logs", exchange_type="fanout")
 
message = "This is a test message"
channel.basic_publish(exchange="logs",routing_key="",body=message)



# 主题交换机。Direct交换器提供了一对一的消息传递，而Topic交换器则提供了基于模式的匹配，适用于一对多的消息传递场景。
# routing_key可以使用*（匹配一个单词） #（匹配多个单词）作为通配符
channel.exchange_declare(exchange="topic_logs", exchange_type="topic")
 
routing_key = "user.delete"
message = "This is a user delete message"
channel.basic_publish(exchange="topic_logs",routing_key=routing_key,body=message)



# 头交换机
channel.exchange_declare(exchange="headers_logs", exchange_type="headers")
 
headers = {"header1": "value1", "header2": "value2"}
message = "This is a headers message"
channel.basic_publish(exchange="headers_logs",routing_key="",body=message,properties=pika.BasicProperties(headers=headers))
                      


# 只能一个消费者   
channel.queue_declare(queue="hello")         
channel.basic_publish(exchange="", routing_key="hello",body="hello world")          

# 可以在发送消息时设置持久化，接收消息时进行确认


conn.close() 
                     