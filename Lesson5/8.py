# print('*******')
# print('*******')
# print('*******')
# print('*******')
# print('*******')

# print(7*'*')
# print(7*'*')
# print(7*'*')
# print(7*'*')
# print(7*'*')

# for i in range (5):
#     print(7*'*')
# print()
# for i in range (5):
#     print(7*'*')
# print()
# for i in range (5):
#     print(7*'*')

def draw_box():
    for i in range(5):
        print(7 * '*')

draw_box()
print()
draw_box()
print()
draw_box()

def print_message():
    print('я  - Полина')
    print('привет')

print_message()

def draw_box2(height,width):
    for i in range(height):
        print(width*'*')

draw_box2(12,5)
print()
draw_box2(2,10)
print()
draw_box2(1,1)
print()

draw_box2(5,5)
print()

draw_box2(6,1)
print()
n= 10
m=10
draw_box2(n,m)