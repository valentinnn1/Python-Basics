import json
with open ("file1.txt", "a") as f:
    for i in range (1, 6):
        State=input("State["+str(i)+"]:")
        Ter=input("Territory["+str(i)+"]:")
        cap=input("Capital["+str(i)+"]:")
        f.write(State+'\t'+Ter+'\t'+cap+'\n')
    f.close()
    
with open ("file2.txt", "a") as f1:
    for i in range (1, 6):
        St=input("State["+str(i)+"]:")
        Pop=input("Population["+str(i)+"]:")
        f1.write(St+'\t'+Pop+'\n')
    f1.close()
    
with open ("file1.txt", "r") as f2:
    for line in f2:
        js=json.dumps(line)
        print(js)
    f2.close()
    
with open ("file2.txt", "r") as f3:
    for line in f3:
        js=json.dumps(line)
        print(js)
    f3.close()

with open ("file1.txt", "r") as f4:
    for line in f4:
        cdata=line.encode('utf-8')
        print(cdata)
    f4.close()
    
with open ("file2.txt", "r") as f5:
    for line in f5:
        bdata=line.encode('utf-8')
        print(bdata)
    f5.close()