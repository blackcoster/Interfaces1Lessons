def bulka(func):
    def wrapper():
        print('булка')
        func()
        print('булка')
    return wrapper

def filling(func):
    def wrapper():
        print('помидоры')
        func()
        print('салат')
    return wrapper

@bulka
@filling
def buter():
    print('котлета')

buter()

# a = bulka(filling(buter))
# a()