def addition(num1,num2):
    print(num1+num2)
def subtraction(num1,num2):
    print(num1-num2)
def multiplication(num1,num2):
    print(num1*num2)
def devision(num1,num2):
    print(num1/num2)

operation = input('Въведете вид операция (+),(-),(*),(/): ')
num1 = int(input("Число 1: "))
num2 = int(input("Число 2: "))

if(operation == '+'):
    addition(num1,num2)
elif(operation == '-'):
    subtraction(num1,num2)
elif(operation == '*'):
    multiplication(num1,num2)
else:
    devision(num1,num2)
