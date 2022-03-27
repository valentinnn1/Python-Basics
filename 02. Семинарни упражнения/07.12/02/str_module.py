import str_module as sm

op=input("+(concatenate)/*(umnozhenie)/-(invert)/p(palindrom)/ord(symboles ascii code)/s(sum of ascii codes):")
if op=="+":
    st1=input("text 1:")
    st2=input("text 2:")
    print(sm.conc(st1, st2))

if op=="*":
    st1=input("text:")
    k=int(input("umnozhi s:"))
    print(sm.umn(st1, k))

if op=="-":
    st1=input("text:")
    print(sm.invert(st1))

if op=="p":
    st1=input("text:")
    print(sm.palindrom(st1))
    
if op=="ord":
    st1=input("text:")
    print(sm.dict(st1))
    
if op=="s":
    st1=input("text:")
    print(sm.ascii(st1))
