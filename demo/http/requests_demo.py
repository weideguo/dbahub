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

#get带有headers
headers={}
r=requests.get("http://httpbin.org/get",headers=headers)
r.text

#post
#post(url, data=None, json=None, **kwargs)
#为复合字典类型时使用json，直接使用，无须转成字符串
payload = dict(key1='value1', key2='value2')
r = requests.post('http://httpbin.org/post', data=payload)
print(r.text)

#put
#put(url, data=None, **kwargs)
requests.put(url, data=payload)


request(method, url, **kwargs)


#使用代理
proxy_dict = {
    "http": "http://192.168.59.128:443",
    "https": "https://192.168.59.128:443",
    #"https": "http://username:password@proxy_server:proxy_port"
}

session=requests.Session()
r=session.get(url,proxies=proxy_dict)

# 使用session可以自动记录cookie


