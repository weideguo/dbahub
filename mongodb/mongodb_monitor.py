#!/bin/env python
#encoding:utf8
#by wdg@dba in 20170926

import pymongo
import traceback
import time
import os

mongodb_list='/data/mongodb_list'
mongodb_log_dir='/data/mongodb_log'

def get_mongodb_server_status(mongodb_url):
	client=pymongo.MongoClient(mongodb_url)
	return client.admin.command('serverStatus')

def dict_minus(dict1,dict2,interval):
	dict3={}
	for key in dict1.keys():
		dict3[key+'_ps']=(dict2[key]-dict1[key])/interval
	return dict3

# caculate some metrics relate to time, like:
# delete per second ...
def tranform_mongodb_server_status(mongodb_server_status_0,mongodb_server_status_1,interval):
	#opcounters_ps=dict_minus(mongodb_server_status_0['opcounters'],mongodb_server_status_1['opcounters'],interval)
	#mongodb_server_status_0['metrics']['document']
	metric_str_list='metrics|document','network','opcounters','opcountersRepl','locks|Metadata|acquireCount','locks|oplog|acquireCount','locks|Global|acquireCount','locks|Collection|acquireCount','locks|Database|acquireCount'
	
	dict3=mongodb_server_status_1	
	for metric_str in metric_str_list:
		try:
			dict1=mongodb_server_status_0
			dict2=mongodb_server_status_1
			for sub_metric in metric_str.split('|'):
				dict1=dict1[sub_metric]
				dict2=dict2[sub_metric]
			new_metric_value=dict_minus(dict1,dict2,interval)
			
			dict3_str="dict3"
			sub_metric_list=metric_str.split('|')
			
			for sub_metric in sub_metric_list[:-1]:
				dict3_str=dict3_str+"['"+sub_metric+"']"
			new_metric=sub_metric_list[-1]+'_ps'
			eval(dict3_str)[new_metric]=new_metric_value
						
		except:
			traceback.print_exc()
			
	return dict3

def loop_dict_to_flat(loop_dict,flat_dict,key_prefix=''):
	for item in loop_dict.keys():
		if isinstance(loop_dict[item],dict):
			loop_dict_to_flat(loop_dict[item],flat_dict,key_prefix+item+'.')
		else:
			flat_dict_key=key_prefix+item
			flat_dict[flat_dict_key]=loop_dict[item]
	

def dict_to_file(dict_name,output_file,output_method='w'):
	new_dict={}
	loop_dict_to_flat(dict_name,new_dict)
        output_dir=os.path.dirname(output_file)
        if os.path.exists(output_dir)!=True:
                os.makedirs(output_dir)
        with open(output_file,output_method) as f:
                for item in new_dict.keys():
                        item_value = "%s:%s \n" % (item.replace(' ','_'),new_dict[item])
                        f.write(item_value)

def per_mongodb_operation(mongodb_url):
	sleep_time=2
	try:
		mongodb_server_status_0=get_mongodb_server_status(mongodb_url)
		time.sleep(sleep_time)
		mongodb_server_status=get_mongodb_server_status(mongodb_url)
		mongodb_server_status=tranform_mongodb_server_status(mongodb_server_status_0,mongodb_server_status,sleep_time)

	except:
		mongodb_server_status={}
		traceback.print_exc()
	mongodb_log=mongodb_log_dir+'/'+mongodb_url.split('@')[-1].split('://')[-1].split('/')[0].replace(':','_')
	dict_to_file(mongodb_server_status,mongodb_log)


def main():
	f=open(mongodb_list,'r')
	l = f.readlines()
	f.close()
	for line in l:
		mongodb_url=line.replace('\n','')
		per_mongodb_operation(mongodb_url)	
		
if __name__=='__main__':
	main()

