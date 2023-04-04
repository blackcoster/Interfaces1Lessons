a = 'hello'
b = {'яблоко','томат','груша'}
b = ('яблоко','томат','груша')
b = ['яблоко','томат','груша']
iterator = iter(b)
# iterator = b.__iter__()

print(next(iterator))
print(next(iterator))