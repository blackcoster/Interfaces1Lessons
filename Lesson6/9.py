import csv
filename = 'table.csv'

shop_list = {'картофель':[2,100],
             'яблоки':[3,250],
             'морковь':[1,35]}

with open(filename,'w',encoding='utf-8',newline='') as file:
    writer = csv.DictWriter(file,fieldnames=['name','weight','price'],quoting=csv.QUOTE_ALL)
    writer.writeheader()
    for name,values in sorted(shop_list.items()):
        writer.writerow(dict(name=name,weight = values[0],price = values[1] ))

rows = []
with open(filename,'r',encoding='utf-8') as file:
    reader = csv.reader(file)
    rows = list(reader)

for r in rows:
    print(r)

