import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
	def get(self):
        #self.write("Hello, world, and weideguo")
		a='''
		<a href='http://httpbin.org'>httpbin</a>
		<p>这个是标题</p>
		'''
		self.write(a)
		self.write("Hello, world, and weideguo")

def make_app():
	return tornado.web.Application([
		(r"/", MainHandler),
	])

if __name__ == "__main__":
	app = make_app()
	app.listen(8888)
	print("web server starting...")
	tornado.ioloop.IOLoop.current().start()
	
