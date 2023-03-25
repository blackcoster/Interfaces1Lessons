class Test(list):
    def append(self, object):
        for i in range(len(self)):
            self[i] = self[i]*object
    def pop(self, index):
        print('поп')

a = Test([1,2,3])
a.append(2)
print(a)
a.pop(0)
print(a)
