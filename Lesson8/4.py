class MyClass:
    def __init__(self,name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,value):
        self._name = value

c = MyClass('123')
# print(c._name)

print(c.name)
# c.name('333')
c.name = '333'
print(c.name)
# print(c.name())