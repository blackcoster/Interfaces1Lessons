def decorator(func):
    def wrapper():
        print('сейчас будет маленькая функция')
        func()
    return wrapper

@decorator
def basic():
    print('я маленькая функция ничего не умею')

basic()

