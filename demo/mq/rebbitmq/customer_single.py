import pika


username = "guest"                                                                                    
pwd = "guest"
cred = pika.PlainCredentials(username, pwd)
conn = pika.BlockingConnection(pika.ConnectionParameters("192.168.59.132", credentials=cred))   
channel = conn.channel()                                                                              
                                                                                                      
                                                                                                                                                                                    
#回调函数                                                                                                             
def callback(ch,method,properties,body):                                                                     
    print("recv %s" % body)    


#只能同时存在一个消费  多个会轮询  
channel.queue_declare(queue="hello")                                                                                                                
channel.basic_consume(callback, queue="hello", no_ack=True)                                                     
     
     
#阻塞循环获取                                                                     
channel.start_consuming()   
