my_dict = {'data1':12, 'data2':8,'data3':12,'data4':45}
ans = 1

for k,v in my_dict.items():
    ans = ans*v

# for i in my_dict:
#     ans *= my_dict[i]

print(ans)