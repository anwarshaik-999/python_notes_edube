x=int(input('enter a number:'))
y=''
while(x/2!=0):
    y+=str(x%2)
    x//=2
print(''.join(reversed(y)))
z=reversed(y)
print(type(z))
for i in z:
    print(i)
    print(type(i))
print(type(''.join(reversed(y))))
print(' '.join(reversed('anwar')))
for i in reversed('anwar'):
    print(i)