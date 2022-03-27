def nullifier(l,n):
    for i in range(0,len(l)):
        if l[i]>n:
            l[i]=0
    print(l)
listChisla= []
br= int(input("Broi chisla v lista: "))
for i in range (0,br):
    listChisla.append(int(input("Chislo v list: ")))
n = int(input("Chislo za sravnenie: "))
nullifier(listChisla,n)