a = int(input('введите а'))
b = int(input('введите б'))
summ = 0
kolichestvo = 0
for i in range(b+1):
    if i%2==0:
        summ+=i
        kolichestvo+=1
# 2 3 4 5 6 =20/5
print(summ/kolichestvo)