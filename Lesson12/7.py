try:
    f = open('1.txt')
    spisok = []
except FileNotFoundError:
    print('файла нет')


try:
    for line in f:
        spisok.append(int(line))
except ValueError:
    print('в файле не число')
except NameError:
    print('проверь код')
except:
    print('мы не знаем что это')
finally:
    f.close()
    print('я закрыл файл')
print(spisok)