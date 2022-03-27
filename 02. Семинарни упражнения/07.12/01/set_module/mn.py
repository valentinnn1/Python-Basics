def mn(s1):
    lst=[]
    lst.append(s1)
    for i in s1:
        mn1=set(str(i))
        lst.append(mn1)
    return lst