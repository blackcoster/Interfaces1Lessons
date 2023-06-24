

def func(n):
    sum = 0
    n-=1
    while n>0:
        sum+= n*n*n
        n-=1
    return sum

print(f'Your sum is: {func(46)}')
