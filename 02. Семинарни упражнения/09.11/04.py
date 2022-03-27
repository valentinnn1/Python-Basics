txt = input('Въведете текст: ')
list1 = []
dic = {}
for i in txt:
    list1.append(ord(i))
print(list1)
tup1 = tuple(sorted(list1))
print(tup1)
for i in list1:
    k = i-62
    alp = 'a'
    if k >= 26:
        alp_text = []
        for a in range(26):
            alp_text.append(alp)
            alp = chr(ord(alp)+1)
        alp_text = ','.join(alp_text)
        dic[i] = alp_text
    if k < 26:
        alp_text = []
        for a in range(1, k+1):
            alp_text.append(alp)
            alp = chr(ord(alp)+1)
        alp_text = ','.join(alp_text)
        dic[i] = alp_text
print(dic)
