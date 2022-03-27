str1 = input()
str2 = input()
str3 = input()

def plus(str1,str2):
    print(str1+str2)

def star(str1,str2):
    sum=0
    for i in str2:
        sum+=ord(i)
    sum=sum-len(str2)*80
    result = str1 * sum
    print(result)
    print(sum)

if(str3 == '*'):
    star(str1,str2)
if(str3 == '+'):
    plus(str1,str2)