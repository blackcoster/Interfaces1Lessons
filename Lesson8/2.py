class Car:
    def __init__(self,color,speed=0,owner=None):
        self.color = color
        self.speed = speed
        self.owner = owner

    def say_owner(self):
        if self.owner==None:
            print('нет хозяина')
        else:
            print(f'мой хозяин {self.owner}')


car1 = Car('red',120)
car2 = Car('red',120,'polina')
car3 = Car('red', owner = 'polina')
car4 = Car(owner='dasha',color='yellow')

car1.say_owner()
car4.say_owner()
# print(car1.speed)
# car2.color = 'yellow'