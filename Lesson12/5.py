import time
from functools import cache

@cache
def func(n):
    res = 0
    for i in range(n):
        res+=i
    return res

start = time.time()
print(func(50_000_000))
end = time.time()
print(end-start)


start = time.time()
print(func(50_000_001))
end = time.time()
print(end-start)