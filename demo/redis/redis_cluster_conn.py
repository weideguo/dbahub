from rediscluster import RedisCluster

"""
pip install redis-py-cluster
"""

# Requires at least one node for cluster discovery. Multiple nodes is recommended.
startup_nodes = [{"host": "127.0.0.1", "port": "7000"}, {"host": "127.0.0.1", "port": "7001"}]
rc = RedisCluster(startup_nodes=startup_nodes, decode_responses=True)
#rc = RedisCluster(startup_nodes=startup_nodes, password='my_redis_passwd', decode_responses=True)

# Or you can use the simpler format of providing one node same way as with a Redis() instance
#rc = RedisCluster(host="127.0.0.1", port=7000, decode_responses=True)

rc.set("foo", "bar")

print(rc.get("foo"))

