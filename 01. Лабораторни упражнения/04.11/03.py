txt = input("Text: ")
dict = {}
for i in txt:
    a = txt.count(i)
    dict[i] = a
print(dict)