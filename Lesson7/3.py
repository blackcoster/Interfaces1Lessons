class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def say_name(self):
        print(f'Меня зовут {self.name}')


chel1 = Person('Polina',22)
chel2 = Person('Daniil',23)
print(chel2.age)
chel1.say_name()
chel2.say_name()
print(type(chel2))