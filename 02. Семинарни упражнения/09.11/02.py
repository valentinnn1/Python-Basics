txt = input('Въведете текст: ')
d = dict()
for i in range(0,len(txt)):
    d[txt[i]]=ord(txt[i])
print(d)