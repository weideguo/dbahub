from redis.sentinel import Sentinel

"""
redis客户端可以多次获取，不会被多次实例化
自动保持tcp连接
"""

#mymaster 为假设的master-name
sentinel = Sentinel([('127.0.0.1', 26379),('127.0.0.1', 26380)], socket_timeout=0.1)

#如果发生切换，内置pool，不再需要再次调用master_for/slave_for，但需要一定的时间等待切换
#客户端线程/进程安全 可以多个并发使用
master = sentinel.master_for('mymaster', password="redis_password",db=0)
master.set('foo', 'bar')

slave = sentinel.slave_for('mymaster', password="redis_password",db=0)
slave.get('foo')

##################
master_addr=sentinel.discover_master('mymaster')
master=redis.Redis(host=master_addr[0],port=master_addr[1],password='redis_password')

slave_addr=sentinel.discover_slaves('mymaster')
slave=redis.Redis(host=slave_addr[0][0],port=slave_addr[0][1],password='redis_password')
