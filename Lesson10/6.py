class MyClass:
    def __init__(self,start):
        self.start = start

    def __iter__(self):
        n = self.start
        while n>0:
            yield n
            n-=1


obj = MyClass(5)

result =  obj.__iter__()

for n in result:
    print(n)