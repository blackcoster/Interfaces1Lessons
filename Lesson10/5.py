def func(num):
    while num>0:
        yield num
        num-=1

for a in func(5):
    if a==3:
        break
    print(a)