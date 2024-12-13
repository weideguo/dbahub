def a():
    yield 1
    yield 2
    yield 3


def b():
    yield 0
    yield from a()    

for x in b():
    print(x)

