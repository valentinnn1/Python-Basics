import set_module as sm
se1=set()
se2=set()
op=input("obedinenie/sechenie/razlika/simetrichna razlika/set:")
if op=="obedinenie": 
    n=int(input("n="))
    for i in range(0, n):
        k=int(input("1. ["+str(i+1)+"]:"))
        se1.add(k)
        
        k=int(input("2. ["+str(i+1)+"]:"))
        se2.add(k)
        
    print(sm.obedinenie(se1, se2))

if op=="sechenie":
    n=int(input("n="))
    for i in range(0, n):
        k=int(input("1. ["+str(i+1)+"]:"))
        se1.add(k)
    x=int(input("dolna granica:"))
    y=int(input("gorna granica:"))
    print(sm.sechenie(se1, x, y))

if op=="razlika":
    n=int(input("n="))
    for i in range(0, n):
        k=int(input("1. ["+str(i+1)+"]:"))
        se1.add(k)
        
        k=int(input("2. ["+str(i+1)+"]:"))
        se2.add(k)
    print(sm.razlika(se1, se2))

if op=="simetrichna razlika":
    n=int(input("n="))
    for i in range(0, n):
        k=int(input("1. ["+str(i+1)+"]:"))
        se1.add(k)
        
        k=int(input("2. ["+str(i+1)+"]:"))
        se2.add(k)
    print(sm.sim_razlika(se1, se2))
    
if op=="set":
    n=int(input("n="))
    for i in range(0, n):
        k=int(input("1. ["+str(i+1)+"]:"))
        se1.add(k)
    print(sm.mn(se1))