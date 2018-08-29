#--encoding=utf-8
import memcache

client=memcache.Client(['192.168.1.1:11211'],debug=0)

client.set("name","wwwww")

value=client.get("name")
client.replace("name","wwwww")
client.delete("name")


client.get_stats()  
client.get_slab_stats() 
