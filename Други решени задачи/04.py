text=input("Enter text:")
list2=[]
dic1={}
for i in text:
    if i!=" ":
        list2.append(ord(i))
tup1=tuple(sorted(list2))
for x in text:
    k=ord(x)-80
    if k>=0:
        dic1[x]=[chr(z) for z in range(97,97+k) if z<123]
    else:
        dic1[x]=[chr(z) for z in range(122,122+k,-1) if z>96]
print(list2)
print(tup1)
print(dic1)