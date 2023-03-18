import csv
filename = 'table.csv'

shop_list = {'картофель':[2,100],
             'яблоки':[3,250],
             'морковь':[1,35]}

with open(filename,'w',encoding='utf-8',newline='') as file:
    writer = csv.writer(file,quoting=csv.QUOTE_ALL)
    writer.writerow(['наименование','вес','цена'])
    for names,values in sorted(shop_list.items()):
        writer.writerow([names,*values])
    writer.writerow(['баклажаны','10','99'])

rows = []
with open(filename,'r',encoding='utf-8') as file:
    reader = csv.reader(file)
    rows = list(reader)

for r in rows:
    print(r)

