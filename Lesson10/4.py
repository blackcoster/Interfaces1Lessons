def func():
    yield 37
    return 42

result = func()

print(result)
print(next(result))
print(next(result))