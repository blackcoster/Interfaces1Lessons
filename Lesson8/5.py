class Parent:
    def say_hello(self):
        print('hello i am parent')

class Child(Parent):
    def say_hello(self):
        print('hello i am child')

c = Child()
p= Parent()
c.say_hello()
p.say_hello()