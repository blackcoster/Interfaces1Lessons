import random

# secret_number = 5
secret_number = random.randint(0,10)
attempts = 3

print('Это программа угадай число. ')

while attempts>0:
    # print('у вас '+ str(attempts) + ' попыток')
    print(f'у вас {attempts}  попыток')
    attempts = attempts-1
    user_number = int(input('введите число - '))

    if user_number == secret_number:
        print('Молодец')
        break
    if user_number > secret_number:
        print('загаданнное число меньше')
    if user_number < secret_number:
        print('загаданнное число больше')

print('Игра окончена')
