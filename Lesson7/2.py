class Animal:
    tip = 'собака'
    age = 2

    def sleep(self):
        print('я сплю')

tuzik = Animal()
sharik = Animal()
sharik.age = 6
print(tuzik.age)
print(sharik.age)
tuzik.sleep()
sharik.sleep()
