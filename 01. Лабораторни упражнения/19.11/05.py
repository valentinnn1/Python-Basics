def nullifier(l,n):
    myDict={}
    for i in range(0,len(l)):
        if l[i]<n:
            myDict[l[i]]=0
        else:
            myDict[l[i]]=l[i]
    print(myDict)
listChisla= []
br= int(input("Broi chisla v lista: "))
for i in range (0,br):
    listChisla.append(int(input("Chislo v list: ")))
n = int(input("Chislo za sravnenie: "))
nullifier(listChisla,n)