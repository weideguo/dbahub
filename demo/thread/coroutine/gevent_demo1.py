import time
from gevent import monkey
monkey.patch_all()
import gevent
import requests

def f(url):
    print('GET: %s' % url)
    r = requests.get(url)
    data = r.text
    print('%d bytes received from %s.' % (len(data), url))

x=time.time()
gevent.joinall([
        gevent.spawn(f, 'https://www.python.org/'),
        gevent.spawn(f, 'https://www.yahoo.com/'),
        gevent.spawn(f, 'https://github.com/'),
])
print(time.time() - x)


x=time.time()
for url in ['https://www.python.org/','https://www.yahoo.com/','https://github.com/']:
    f(url)
 
print(time.time() - x)
