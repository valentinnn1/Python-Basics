text=input("Enter text:")
list2=[]
list3=[]
for i in text:
    if i!=" ":
        list2.append(i)
tup1=tuple(list2)
tup2=tuple(list2[::-1])
for x in list2:
    list3.append(ord(x))
tup3=tuple(list3)
tup4=tuple(sorted(list3))
print(text)
print(tup1)
print(tup2)
print(tup3)
print(tup4)