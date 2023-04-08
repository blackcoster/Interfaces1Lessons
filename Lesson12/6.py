# num1 = int(input())
# num2 = int(input())
# print(num1/num2)

# a =
# b=
# p = a+b
# s = a*b
# print(f'площадь {s}')
try:
    num1 = int(input())
    num2 = int(input())
    result = num1/num2
except ZeroDivisionError:
    result = 'не делите на ноль!'
except ValueError:
    result = 'нцжны числа'
except :
    result = 'какая-то другая ошибка'
finally:
    print('закончили')
print(result)