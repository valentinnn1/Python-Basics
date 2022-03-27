import random
list=[]
listeven=[]
listodd=[]

for i in range(1, 11):
    list.append(random.randint(1, 10))

for even in range(0,len(list),2):
    listeven.append(list[even])

for odd in range(1,len(list),2):
    listodd.append(list[odd])

listeven.sort()
listodd.sort(reverse=True)
print(list)
print(listeven)
print(listodd)