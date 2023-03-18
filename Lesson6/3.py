# file = open('example.txt','r')
# print(file.read())
# file.close()


# r - чтение
# w - только запись (перезаписывает)
# a - добавление содержимого


# file =open('example.txt','a')
# file.write('\npython')
# file.close()
# file = open('example.txt','r')
# print(file.read())
# file.close()


file =open('example.txt','w')
file.write('\npython')
file.close()
file = open('example.txt','r')
print(file.read())
file.close()
