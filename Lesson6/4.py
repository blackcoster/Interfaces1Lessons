# with open('example.txt') as file:
#     print(file.read())

f = open('example.txt','r')
# a = f.read(7)
# b = f.read(7)
# print(b)

# a = f.readline()
a = f.readlines()

print(a)

file = open('polina.txt','w')
file.write('Hello')
file.close

with open ('example.txt') as file:
    for t in file:
        print(t.strip())
