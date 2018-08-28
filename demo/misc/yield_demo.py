def f(n):
    for i in range(n):
        yield i*i
			
			
a=f(10)
for x in a:
    print x
