class MyRange:
    def __init__(self,start,stop,step):
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        x = self.start
        while x<self.stop:
            yield x
            x+=self.step

nums = MyRange(1,10,2)
for x in nums:
    print(x)
