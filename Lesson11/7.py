def decorator(func):
    def wrapper():
        print('прошлое')
        func()
        print('будущее')


    return wrapper

@decorator
def timing():
    print('настоящее')

timing()
