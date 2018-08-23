import Pyro4

uri=''					###服务端的uri
gmc=Pyro4.Proxy(uri)
gmc.say_hi()
