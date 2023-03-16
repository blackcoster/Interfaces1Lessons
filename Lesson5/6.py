a = {"ключ":'значение'}

quads = {1:1,
         2:4,
         3:9,
         4:16,
         5:25}
print(quads[5])
a={}
print(type(a))
a = {'a':1, 'b':2}
print(a['a'])

a = dict([(1,2),(3,4)])
print(a)
b = a.copy()
# a.clear()
# print(a)

# get(key,default)
a = {1:1000}
print(a.get(1,3))
print(a.get(5,3))

print(quads.items())
# for k,v in quads.items():

a = {2:1,'a':4}
print(a.keys())

a = {2:1,'a':4}
print(a.values())

# b = a.pop('a')
# b = a.popitem()

a.setdefault(2)
a.update({'b':5})
print(a)

for x in a:
    print(a[x])

for k,v in a.items():
    print(k,v)

