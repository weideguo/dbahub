# pip install redis 
# 不再使用第三方包实现对cluster连接

from redis.cluster import RedisCluster as Redis
from redis.cluster import ClusterNode

_nodes = [
("10.0.0.1",6379),
("10.0.0.2",6379),
("10.0.0.3",6379),
("10.0.0.4",6379),
("10.0.0.5",6379),
("10.0.0.6",6379),
]


nodes = [ ClusterNode(n[0],n[1]) for n in _nodes]

# nodes = [ClusterNode('localhost', 6379), ClusterNode('localhost', 6378)]

password ="w12345"
db=0
decode_responses=True
encoding_errors="ignore"
retry_on_timeout=True
max_connections=5
timeout=None


rc = Redis(startup_nodes=nodes,
password=password,
decode_responses=decode_responses, 
encoding_errors=encoding_errors,
retry_on_timeout=retry_on_timeout,
max_connections=max_connections,
timeout=timeout
)


rc.info()

rc.scan(0)


