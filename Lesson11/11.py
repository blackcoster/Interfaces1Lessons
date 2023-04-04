def decorator(func):
    def wrapper(*args):
        print('привет')
        func(*args)
        print('пока')

    return wrapper

@decorator
def my_name_is(*args):
    print(*args )

my_name_is('polina','маша','lena','vika')
my_name_is('polina')
