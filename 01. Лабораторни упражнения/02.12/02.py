import math

try:
    num = int(input('Enter a number: '))
    print(math.sqrt(num))
except:
    print('Invalid Number')
finally:
    print('Good Bye')