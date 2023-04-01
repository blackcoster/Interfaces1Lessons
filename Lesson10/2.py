file = open('test.txt')

lines = (t.strip() for t in file  if t[0]=='#')

# comments = (t for t in lines if t[0]=='#')

for c in lines:
    print(c)

lineslist = list(lines)
print(lineslist)