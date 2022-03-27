def nullifier(l,n):
    myDict={}
    for i in range(0,len(l)):
        if l[i]<n:
            myDict[l[i]]=0
        else:
            myDict[l[i]]=l[i]
    print(myDict)

list= []
count= int(input("Element count in list: "))
for i in range (0,count):
    list.append(int(input(f'Element {i+1} in list: ')))
n = int(input("n = "))

nullifier(list,n)