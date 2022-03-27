text=input("Enter text:")
dic1={}
for i in text:
    a=ord(i)
    b=0
    for x in str(a):
        b+=int(x)
        dic1[ord(i)]=b
print(dic1)