class Animal:
    def __init__(self,name,breed='без породы'):
        self.name = name
        self.breed = breed

    def __say_breed(self):
        print(f' я {self.breed}')

a = Animal('barsik')
b = Animal('Вильгельмина-Афродита','абиссинская')
a._Animal__say_breed()
b._Animal__say_breed()