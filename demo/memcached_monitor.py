#!/bin/env python
#encoding:utf8
#by wdg@dba in 20171013

import memcache
import os
import time

"""
vim memcached_list
127.0.0.1|11211
"""

memcached_list="/data/memcached_list"
memcached_log_dir="/data/memcached_log"

def dict_to_file(dict_name,output_file,output_method='w'):
	output_dir=os.path.dirname(output_file)
	if os.path.exists(output_dir)!=True:
		os.makedirs(output_dir)
	with open(output_file,output_method) as f:
		for item in dict_name.keys():
			item_value = "%s %s \n" % (item,dict_name[item])
			f.write(item_value)

def get_info(memcached_client,sleep_sec=30):
	memcached_info=memcached_client.get_stats()[0][1]
	time.sleep(sleep_sec)
	memcached_info_1=memcached_client.get_stats()[0][1]
	
	memcached_info['cmd_set_ps']=(int(memcached_info_1['cmd_set'])-int(memcached_info['cmd_set']))/sleep_sec
	memcached_info['cmd_get_ps']=(int(memcached_info_1['cmd_get'])-int(memcached_info['cmd_get']))/sleep_sec
	memcached_info['bytes_read_ps']=(int(memcached_info_1['bytes_read'])-int(memcached_info['bytes_read']))/sleep_sec
	memcached_info['bytes_written_ps']=(int(memcached_info_1['bytes_written'])-int(memcached_info['bytes_written']))/sleep_sec

	return memcached_info
		

def main():
	f = open(memcached_list,'r')
	l = f.readlines()
	f.close()
	for line in l:
		host,port=line.replace('\n','').split('|')
		memcached_client=memcache.Client([host+':'+str(port)])
		memcached_info=get_info(memcached_client)
		memcached_log_file="%s/%s_%s"%(memcached_log_dir,host,str(port))
		dict_to_file(memcached_info,memcached_log_file)

if __name__=='__main__':
	main()	
