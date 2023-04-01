def func(num):
    while num>0:
        yield num
        # yield num**2
        num-=1

# print(func(5))

# for num in func(3):
#     print(num)
result = func(5)

a = sum(result)
print(a)

# print(next(result))
# print(next(result))
# print(next(result))
# print(next(func(5)))
# print(next(func(5)))
# print(next(func(5)))
# print(next(func(5)))
# print(next(func(5)))
# print(next(func(5)))
#
# print(result.__next__())
# print(next(result))