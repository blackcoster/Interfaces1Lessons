dict1 = {1:1,
         2:4,
         3:9}

dict1 = {x:x**2 for x in range(1,10)}

dict1 = {x:x**2 for x in [1,2,5]}

dict1 = {x:y for x in [1,2,3] for y in 'ABC'}
dict1 = {x:y for x in [1,2,3] for y in 'C'}
dict1 = {x:[y for y in [1,2,3]] for x in range(5)}
dict1 = {x:{y:x for y in 'xyz'} for x in 'abc'}
dict1 = {x:y for x in [1,2,3,4,5,6] for y in range(4,10) if x==y}
# 1:a
# 1:b
# 1: c
# 2:a
# 2:b
print(dict1)



#set множество {1,2,3}
#tuple кортеж (1,2,3)
#list список [1,2,3]
#dict словарь {1:2,2:4}