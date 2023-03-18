import json

filename = 'file.json'

info = {'имя':'полина',
        'фамилия':'крупенина',
        'возраст':23,
        'хобби':['программирование','теннис']}

with open(filename,'w',encoding='utf-8') as file:
    file.write(json.dumps(info,ensure_ascii=False,indent=4))

info2 =[]
with open(filename,encoding='utf-8') as file:
    info2 = json.loads(file.read())

print(info2)