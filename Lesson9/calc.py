def add(num1,num2):
    return num1+num2

def sub(num1,num2):
    return num1-num2

def mul(num1,num2):
    return num1*num2

def div(num1,num2):
    if num2==0:
        return 'нельзя'
    return num1//num2

if __name__ =='__main__':
    print('я запущен как основной файл')
