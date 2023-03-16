a = [2,4,6,8]
a.append(2)
print(a)
a.remove(2) #по значению
print(a)
b = a.pop(2) #по индексу
print(a)
print(b)
a = [1,2,3,7,5]
# a.clear()
# print(a)
a.sort()
print(a)

a = [1,2,3]
b= [3,5,6]
a.extend(b)
print(a)

print(b.index(6))

a = [2,1,3]
a.insert(0,9)
print(a)