input = input()
dict = {}

for i in input:
    code = ord(i)
    codetostr = str(code)
    if(codetostr==codetostr[::-1]):
        dict[code]=1
    else:
        dict[code]=0
print(dict)