import random

elements = int(input('Брой на елементи: '))
list1 = []
b = 0

for i in range(elements):
    a = round(random.uniform(0, 100))
    list1.append(a)

list2 = list1

for n in range(elements):
    if n+1 == elements:
        break
    sum = list2[n] + list2[n+1]
    list1.insert(n+1+b, sum)
    b += 1
print(list1)
