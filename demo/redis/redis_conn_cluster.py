#!/bin/env python

from rediscluster import StrictRedisCluster
#coding:utf8

#
startup_nodes=[{"host":"127.0.0.1","port":"7000"},{"host":"127.0.0.1","port":"7001"},{"host":"127.0.0.1","port":"7002"}]

rc=StrictRedisCluster(startup_nodes=startup_nodes,decode_response=True)
rc.get('name')
