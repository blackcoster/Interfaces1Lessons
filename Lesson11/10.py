def decorator(func):
    def wrapper(name):
        print('привет')
        func(name)
        print('пока')

    return wrapper

@decorator
def my_name_is(name):
    print(f'меня зовут {name}' )

my_name_is('polina')

#
# class Decorator:
#     def __init__(self,func):
#         self.func = func
#
#     def __call__(self, name):
#         print('привет')
#         self.func(name)
#         print('пока')
#
# @Decorator
# def my_name_is(name):
#     print(f'меня зовут {name}' )
#
# my_name_is('masha')