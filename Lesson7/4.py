class Transport:
    def __init__(self,color,weight):
        self.color = color
        self.weight = weight

    def beep(self):
        print('бип')

class Car(Transport):
    def __init__(self,color,weight,owner):
        super().__init__(color,weight)
        self.owner = owner

    def say_owner(self):
        print(f'Мой владелец {self.owner}')
#
class Bus(Transport):
    def __init__(self,color,weight,driver):
        super().__init__(color,weight)
        self.driver = driver

    def opendoors(self):
        print('doors are opened')

    def say_driver(self):
        print(f'мой водитель - {self.driver}')

t1 = Transport('red',1000)
t1.beep()
car1 = Car('blue',500,'polina')
car1.beep()
car1.say_owner()

bus211 = Bus('yellow','2000','Александр')
bus211.say_driver()
bus211.opendoors()

