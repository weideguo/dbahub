import pika


username = "guest"                                                                                    
pwd = "guest"
cred = pika.PlainCredentials(username, pwd)
conn = pika.BlockingConnection(pika.ConnectionParameters("192.168.59.132", credentials=cred))   
channel = conn.channel()                                                                              
                                                                                                      
                                                                                                                                                                                    
#回调函数                                                                                                             
def callback(ch,method,properties,body):                                                                     
    print("recv %s" % body)                                                                         
      
      
#广播的接收      
channel.exchange_declare(exchange="logs",exchange_type="fanout")
result = channel.queue_declare(exclusive=True)          
queue_name = result.method.queue                        
channel.queue_bind(exchange="logs",queue=queue_name)

channel.basic_consume(callback, queue=queue_name, no_ack=True)                                                     

     
#阻塞循环获取                                                                     
channel.start_consuming() 
