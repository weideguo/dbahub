#!/usr/local/python/bin/python
#encoding:utf8
#by wdg@dba in 20170921

import redis
import os
import traceback

redis_list="/data/redis_list"
redis_log_dir="/data/redis/redis_log"

def dict_to_file(dict_name,output_file,output_method='w'):
	output_dir=os.path.dirname(output_file)
	if os.path.exists(output_dir)!=True:
		os.makedirs(output_dir)
	with open(output_file,output_method) as f:
		for item in dict_name.keys():
			item_value = "%s %s \n" % (item,dict_name[item])
			f.write(item_value)

def get_info_n_config(redis_client):
	redis_info=redis_client.info()
	redis_config=redis_client.config_get()
	
	#calculate used memory percent
	memory_percent=round(float(redis_info['used_memory'])/float(redis_config['maxmemory']),4)
	connected_clients_percent=round(float(redis_info['connected_clients'])/float(redis_config['maxclients']),4)
		
	info_n_config=dict(redis_info,**redis_config)
	info_n_config=dict(info_n_config,used_memory_percent=memory_percent)
	info_n_config=dict(info_n_config,connected_clients_percent=connected_clients_percent)
	return info_n_config
		

def get_redis_client(host,port,password):
	try:
		redis_client=redis.Redis(host=host,port=port,password=password,db=0)
	except:
		redis_client=redis.Redis(host=host,port=port,db=0)
	return redis_client

def main():
	f = open(redis_list,'r')
	l = f.readlines()
	f.close()
	for line in l:
		try:
			host,port,password=line.replace('\n','').split('|')
			redis_client=get_redis_client(host,port,password)
			info_n_config=get_info_n_config(redis_client)
			redis_log_file="%s/%s_%s"%(redis_log_dir,host,str(port))
			dict_to_file(info_n_config,redis_log_file)
		except:
			traceback.print_exc()

if __name__=='__main__':
	main()	
