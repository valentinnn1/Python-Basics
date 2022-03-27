str1 = input()
str2 = input()
str3 = input()

def plus(str1,str2):
    print(str1+str2)

def star(str1,str2):
    result = str1 * len(str2)
    print(result)

if(str3 == '*'):
    star(str1,str2)
if(str3 == '+'):
    plus(str1,str2)