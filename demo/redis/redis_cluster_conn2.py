#!/bin/env python
#coding:utf8

# old
from rediscluster import StrictRedisCluster

startup_nodes=[{"host":"127.0.0.1","port":"7000"},{"host":"127.0.0.1","port":"7001"},{"host":"127.0.0.1","port":"7002"}]

rc=StrictRedisCluster(startup_nodes=startup_nodes,decode_response=True)
rc.get('name')

# new
from rediscluster import RedisCluster


RedisCluster(host=None, port=None, startup_nodes=None, max_connections=None, max_connections_per_node=False, init_slot_cache=True, readonly_mode=False, reinitialize_steps=None, skip_full_coverage_check=False, nodemanager_follow_cluster=False, connection_class=None, read_from_replicas=False, cluster_down_retry_attempts=3, host_port_remap=None, **kwargs)


redis_password = "my_redis_passwd"
rc = RedisCluster(startup_nodes=startup_nodes, password=redis_password, decode_responses=True)

