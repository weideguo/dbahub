import pika


username = "guest"                                                                                    
pwd = "guest"
cred = pika.PlainCredentials(username, pwd)
#conn = pika.BlockingConnection(pika.ConnectionParameters("192.168.59.132", credentials=cred))   
conn = pika.BlockingConnection(pika.ConnectionParameters(host=["192.168.59.132:5672"], credentials=cred))   
channel = conn.channel()                                                                             


#这样方式发送只能一个消费者接受   
channel.queue_declare(queue="hello")         
channel.basic_publish(exchange="", routing_key="hello",body="hello world")                              


#实现广播                                                                                                
channel.exchange_declare(exchange="logs",exchange_type="fanout")
channel.basic_publish(exchange="logs", routing_key="",body="hello world")     
  

conn.close()    
