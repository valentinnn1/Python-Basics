txt=input('Въведете текст: ')
d = dict()
sum = 0
for item in txt:
    for i in str(ord(item)):
        sum+= int(i)
    d[ord(item)] = sum
    sum=0
print(d)