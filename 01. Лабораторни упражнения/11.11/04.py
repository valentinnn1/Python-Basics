import random

list1=[]
list2=[]

for i in range(1, 11):
    list1.append(random.randint(1, 10))
    list2.append(random.randint(11, 20))

newlist=[]

for i in range(0, len(list1)):
    newlist.append(list1[i])
    newlist.append(list2[i])
    
print(list1)
print(list2)
print(newlist)