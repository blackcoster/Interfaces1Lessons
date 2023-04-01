def gen1(stop):
    n=1
    while n<=stop:
        yield n
        n+=1   #1 2 3 4 5
def gen2(start):
    n = start
    while n>0:
        yield n
        n-=1 #5 4 3 2 1

# def func(a):
#     for x in gen1(a):
#         yield x
#     for x in gen2(a):
#         yield x

def func(a):
    yield from gen1(a)
    yield from gen2(a)

for n in func(5):
    print(n)