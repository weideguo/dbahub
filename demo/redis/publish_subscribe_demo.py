import redis
redis_send_pool=redis.ConnectionPool(host="127.0.0.1", port=6379, db=0, password="my_passwd")   
r=redis.StrictRedis(connection_pool=redis_send_pool)

ps=r.pubsub()
ps.psubscribe("kill_host")
ps.listen()
x=ps.parse_response()

r.publish("kill_host","1234")
