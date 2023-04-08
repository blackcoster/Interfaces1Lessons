def decorator_with_args(name):
    print(name)

    def decorator(func):
        def wrapper(a, b):
            print('перед функцией')
            result = func(a, b)
            print('после функции')
            return result

        return wrapper

    return decorator


@decorator_with_args('polina')
def add(a, b):
    print('функция add')
    return a + b


a = add(10, 10)
# print(a)
