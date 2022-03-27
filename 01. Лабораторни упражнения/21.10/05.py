a = int(input('а = '))
b = int(input('b = '))
c = int(input('c = '))

if(a+b > c and b+c > a and a+c > b):
    print('We can have a triangle with this sides!')
else:
    print('Sorry. We cant have a triangle with this sides')
