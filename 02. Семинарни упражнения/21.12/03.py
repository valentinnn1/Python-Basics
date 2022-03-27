st="This is good!"

with open ('document.bin', 'wb') as f:
    cdata=st.encode('utf-8') 
    f.write(cdata)
    f.close()

with open ('document.bin', 'rb') as f1:
    bdata=f1.read()
    for byte in bdata:
        print(byte)
    f.close()