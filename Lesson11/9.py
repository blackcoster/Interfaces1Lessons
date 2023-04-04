class Decorator:
    def __init__(self,func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print('before smol')
        self.func()
        print('after smol')

@Decorator
def smol():
    print('im smol')

smol()