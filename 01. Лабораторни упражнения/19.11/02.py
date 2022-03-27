inputText = input()
dict = dict()

for i in inputText:
    x = str(ord(i))
    if (x == x[::-1]):
        dict[ord(i)]=1
    else:
        dict[ord(i)]=0
print(dict)