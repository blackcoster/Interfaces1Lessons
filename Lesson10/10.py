def func():
    data = bytearray()
    line = None
    linecount = 0
    while True:
        part = yield line
        linecount += part.count(b'\n')
        data.extend(part)
        if linecount>0:
            index = data.index(b'\n')
            line = bytes(data[0:index+1])
            data = data[index+1:]
            linecount-=1
        else:
            line = None





r = func()
print(r.send(None))
print(r.send(b'hello'))
print(r.send(b'world\nit'))
print(r.send(b'works'))
print(r.send(b'world\nit'))
