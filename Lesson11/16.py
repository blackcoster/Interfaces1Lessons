import sys

def dec(func):
    def wrapper(a,b):
        result = sys.getsizeof(func(a,b))
        print(f'занимает в памяти {result} байт')
    return wrapper

@dec
def adder(a,b):
    return a*b

adder(4535792398480288302082804084028842082424,56789765435678657786578)