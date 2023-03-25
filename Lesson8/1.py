# def get_name(name='нет имени'):
#     print(name)
#
# get_name('полина')
# get_name()

class Car:
    def __init__(self,color,speed=0):
        self.color = color
        self.speed = speed

car1 = Car('green')
print(car1.speed)
car2 = Car('blue',120)
print(car2.speed)