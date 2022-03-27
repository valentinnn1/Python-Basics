import binascii

file = open("document.bin", "wb")
Ascii = b"This is good"
file.write(binascii.b2a_uu(Ascii))
file.close()
file = open("document.bin", "rb")
print(file.read())
file.close()