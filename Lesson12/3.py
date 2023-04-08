from functools import wraps


def decorator(func):
    '''декоратор'''


    @wraps(func)
    def wrapper(name):
        '''обертка'''
        func(name)
        print('goodbye')
    return wrapper

@decorator
def hello(name):
    '''функция которая здоровается'''
    print(f'hello {name}')


hello('polina')
print(hello.__doc__)
print(hello.__name__)
# help(hello)