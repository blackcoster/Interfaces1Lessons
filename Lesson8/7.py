# a= 3
# b = 5
# c = a.__add__(b)
# a+b
# c = a.__sub__(b)
# c = a.__mul__(b)
# # c = a.__divmod__(b)
# print(c)

class Test(int):
    def __init__(self,num):
        super().__init__()
        self.num = num
    def __add__(self, other):
        # return self.num*other
        print('хочешь сложить.... вот тебе умножение на два')
        return self.num * 2
a = Test(5)

print(a+1)
# a/6
print(a.__add__(7))

# __add__(self, other) - сложение. x + y.
# __sub__(self, other) - вычитание (x - y).
# __mul__(self, other) - умножение (x * y).
# __truediv__(self, other) - деление (x / y).
# __floordiv__(self, other) - целочисленное деление (x // y).
# __mod__(self, other) - остаток от деления (x % y).
# __divmod__(self, other) - частное и остаток (divmod(x, y)).
# __pow__(self, other[, modulo]) - возведение в степень (x ** y, pow(x, y[, modulo])).
# __iadd__(self, other) - +=.
# __isub__(self, other) - -=.
# __imul__(self, other) - *=.
# __itruediv__(self, other) - /=.
# __ifloordiv__(self, other) - //=.
# __imod__(self, other) - %=.
# __ipow__(self, other[, modulo]) - **=.
