#tuple

a = ()
a = (12,)
a = (1,2)
b = list(a)
b.append(3)
a = tuple(b)
print(a)