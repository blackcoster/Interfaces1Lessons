class Test(str):
    def __init__(self,word):
        super().__init__()
        # self.word = word
    def __len__(self):
        return 25

stroka = Test('3535рыиар')
print(len(stroka))