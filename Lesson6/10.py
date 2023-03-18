import pickle

filename = 'test.txt'

info = {'имя':'полина',
        'фамилия':'крупенина',
        'возраст':23,
        'хобби':['программирование','теннис']}

with open(filename,'wb') as file:
    pickle.dump(info,file)

info1=[]
with open(filename,'rb') as file:
    info1 = pickle.load(file)
    # info1 = file.read()

print(info1)