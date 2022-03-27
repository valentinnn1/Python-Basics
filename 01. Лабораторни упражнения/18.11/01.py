x = int(input('Въведете число (1:квадрат, 2:правоъгълник, 3:прав.триъгълник) : '))

def square(a):
    print(f'S = {a*a:.2f} cm2')

def rectangle(a,b):
    print(f'S = {a*b/2:.2f} cm2')

def triangle(a,b):
    print(f'S = {a*b:.2f} cm2')

if(x==1):
    a = int(input('a = '))
    square(a)
if(x==2):
    a = int(input('a = '))
    b = int(input('b = '))
    rectangle(a,b)
if(x==3):
    a = int(input('a = '))
    b = int(input('b = '))
    triangle(a,b)