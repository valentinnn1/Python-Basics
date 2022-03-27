def sum(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multipl(a,b):
    return a*b
def divide(a,b):
    return a/b
while True:
    try:
        print("Enter the type of operation(+,-,*,/): ")
        operation = input("Enter an operation: ")
        a =float(input("Num1 = "))
        b =float(input("Num2 = "))
        if operation == "+":
            print(sum(a,b))
        elif operation == "-":
            print(subtract(a,b))
        elif operation == "*":
            print(multipl(a,b))
        elif operation == "/":
            print(divide(a,b))
        else:
            raise Exception("Please enter a valid operation!")
        break
    except Exception as OperationError:
        print(OperationError)
    except ValueError:
        print("Enter a number!")
    except ZeroDivisionError:
        print("Devision by zero is not allowed!!!")











