n = int(input())
todo_list = []
for i in range(n):
    delo = input()
    todo_list.append(delo)

print(todo_list)

with open(filename,'a') as file:
    for d in todo_list:
        file.write()

