import random

list1=[]

for i in range(0,3):
    firstnum= random.randint(1,20)
    secondnum = random.randint(1,20)
    sum = firstnum + secondnum
    list1.append(firstnum)
    list1.append(sum)
    list1.append(secondnum)

print(list1)