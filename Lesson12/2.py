class Decorator:
    def __init__(self,name):
        self.name = name
        print(name)

    def __call__(self,func):
        def wrapper(a,b):
            print('до')
            c = func(a,b)
            print('после')
            return c
        return wrapper



@Decorator('test')
def add(a, b):
    print('функция add')
    return a + b


a = add(10, 10)
print(a)

