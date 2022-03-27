text = input('Въведете текст: ')
r = int(input('Въведете число: '))
tup = tuple(text)
elcount = len(tup)
newlist = list()
for x in range(0, elcount,r+1):
    newlist.append(tup[x])
newtup = tuple(newlist)
print(newtup)