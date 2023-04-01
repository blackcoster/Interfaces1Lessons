def func():
    while True:
        n = yield

        print(n)

r = func()
r.send(None)
r.send(5)
r.send(8)
r.send(8)
r.send(8)
r.send(8)
r.close()
r.send(8)

