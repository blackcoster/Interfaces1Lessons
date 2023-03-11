# for i in range(3):
#     for j in range(4):
#         print(i,j)

# for i in range(3):
#     for j in range(4):
#         if i==j:
#             continue
#         print(i,j)

# for i in range(3):
#     for j in range(4):
#         if i==j:
#             break
#         print(i,j)

flag = False
for i in range(3):
    for j in range(3):
        if j==1:
            flag = True
            break
        print(i,j)
    if flag ==True:
        break