# print('даня '* 100)

def danyaprinter(n,name):
    print(f'я написала {name} {n} раз')
    print(name*n)

danyaprinter(10,'полина ')

def kvadrat(height, width):
    print('_'* width)
    for i in range(height-2):
        print ('|'+' '*(width-2)+'|')
    print('_' * width)

kvadrat(5,6)