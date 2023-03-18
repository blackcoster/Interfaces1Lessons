# x = 5
#
# def func():
#    global x
#    x = x*10
#
# func()

# def func():
#    x = 5
#
# func()
# print(x)

def func():
   x = 5
   y=6
   return x,y

a,b = func()

result = func()
# print(result)

def quad(a):
   b = a**2
   return b



result = quad(4)
print(result)