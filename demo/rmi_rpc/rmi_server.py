import Pyro4

class GM(object):
	def say_hi():
		print('hi')
gm=GM()
daemon=Pyro4.Daemon()
uri=daemon.register(gm)
print('uri='+uri)
daemon.requestLoop()
