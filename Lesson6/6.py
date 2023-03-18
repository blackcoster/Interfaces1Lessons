with open('polina.txt') as file:
    str1 =file.read()
word_list = str1.split()
# result = ''
# for word in word_list:
#     result=result+word+', '
result = ', '.join(word_list)
print('pokina\nkrupenina')