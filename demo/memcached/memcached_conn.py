#--encoding=utf-8
import memcache

client=memcache.Client(['192.168.200.141:11211'],debug=0)

client.set("name","weideguo")

value=client.get("name")
client.replace("name","weideguo")
client.delete("name")


client.get_stats()  
client.get_slab_stats() 
