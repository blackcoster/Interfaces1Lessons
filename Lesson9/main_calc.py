from calc import mul,div,sub,add
import calc

class Calculator:
    def __init__(self):
        self.main()

    def main(self):
        print('Это калькулятор')
        while True:
            num1 = int(input('Введите первое число'))
            num2 = int(input('Введите второе число'))
            choice = input('выберите + или - или // или *')
            match choice:
                case '+':
                    print(add(num1,num2))
                case '*':
                    print(mul(num1, num2))
                case '//':
                    print(div(num1, num2))
                case '-':
                    print(sub(num1, num2))
                case _:
                    print('неверно ввели')

if __name__=='__main__':
    calculator = Calculator()
# print(__name__)
# print(calc.__name__)