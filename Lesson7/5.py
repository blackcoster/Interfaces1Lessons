class Human:
    def __init__(self,name):
        self.name = name
    def say(self):
        print('что-то говорю')
    def walk(self):
        print('я хожу')

class Transport:
    def __init__(self,model,speed):
        self.model = model
        self.speed=speed

    def drive(self):
        pass
    def beep(self):
        print('beeep')

class Transformer(Transport,Human):
    pass

bumblebee = Transformer('ferrari',280)

bumblebee.beep()
bumblebee.say()
bumblebee.walk()
bumblebee.name = 'Bumblebee'

