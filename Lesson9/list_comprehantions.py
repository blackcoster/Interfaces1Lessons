a = [1,2,3,4,5,6,7,8,9]

list1 = []
for i in range(1,10):
    list1.append(i)

# print(list1)

list2 = [i for i in range(1,10)]
# print(list2)
list3 = [i*2 for i in range(1,10)]
list3 = [str(i) for i in range(1,10)]
# list3 = [int(i) for i in input().split()]

list3 = [i for i in range(1,50) if i%2==0]

list3 = [i*j for i in range(1,10) for j in [1,6,8] ]

list3 = [i*j for i in range(1,10) for j in [1,6,8] if i*j%2==1 ]
list3 = [i*j for i in range(1,10) if i%2!=0  for j in [-5,1,6,8] if j>0 ]

list3 = [i//2 for i in range(1,101) if i%2==0]
print(list3)

# def unique(spisok):
