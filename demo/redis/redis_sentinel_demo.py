from redis.sentinel import Sentinel


#mymaster 为假设的master-name
sentinel = Sentinel([('127.0.0.1', 26379),('127.0.0.1', 26380)], socket_timeout=0.1)

#认证不得
master = sentinel.master_for('mymaster', socket_timeout=0.1)
master.set('foo', 'bar')

slave = sentinel.slave_for('mymaster', socket_timeout=0.1)
slave.get('foo')

##################
master_addr=sentinel.discover_master('mymaster')
master=redis.Redis(host=master_addr[0],port=master_addr[1],password='hjlr^Y1_')

slave_addr=sentinel.discover_slaves('mymaster')
slave=redis.Redis(host=slave_addr[0][0],port=slave_addr[0][1],password='hjlr^Y1_')
