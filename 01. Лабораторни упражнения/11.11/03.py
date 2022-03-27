import random   
list1=list() 
list2=list()
for i in range(1, 11):
    list1.append(random.randint(1, 10))

for k in range(0,len(list1),2):
    list2.append(list1[k])
    sum = list1[k] + list1[k+1]
    list2.append(sum)
    list2.append(list1[k+1])
print(list2)