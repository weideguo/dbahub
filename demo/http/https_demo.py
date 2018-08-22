import requests
#coding:utf8

'''
https其他方法，安装
pyOpenSSL
pyasn
ndg-httpsclient
'''

#处理因ssl出现的连接错误
a=requests.get('https://wx.qq.com',verify=False)
a.text

#get
#get(url, **kwargs)
r=requests.get("http://httpbin.org/get")
r.text

#post
#post(url, data=None, json=None, **kwargs)
payload = dict(key1='value1', key2='value2')
r = requests.post('http://httpbin.org/post', data=payload)
print(r.text)

#put
#put(url, data=None, **kwargs)
requests.put(url, data=payload)


request(method, url, **kwargs)
