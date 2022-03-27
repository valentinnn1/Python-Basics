n=int(input('Enter a number: '))
list = []
for x in range(1,n+1):
    y = pow(2,x)
    list.append(y)
print(list)