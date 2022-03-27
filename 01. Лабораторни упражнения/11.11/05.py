n = int(input('Въведете число: '))
list= list()
for i in range(1,n+1):
    list.append(i)
reversedlist = list[::-1]

d=dict()

for j in range(0,len(reversedlist)):
    d[list[j]]=reversedlist[j]

print(d)