x=10
y='0b110'
z='0xA1'
#not a case sensitive
O='0o27'
print(int(y,2))
#2 specifies no of letters in binary
print(int(z,16))
#16 in hexadecimal
print(int(O,8))
#8 in octal
print(bin(int(y,2)))
print(type(bin(int(y,2))))
print(oct(int(O,8)))
print(hex(int(z,16)))