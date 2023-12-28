#we cannot modify tuples like tuple.append or del tuple or tuple[0]='value'
tuple1=('anwar','shaik',19)
tuple2='shaik',19,'anwar'
tuple3=3,
tuple4=(4,)
print(tuple1,tuple2,tuple3,tuple4)
notatuple=(1)
print('notatuple:',notatuple)
print('operating tuples')
for element in tuple1:
    print(element,end='_')
print()
for i in range(len(tuple1)):
    print(tuple1[i],end='_')
print()
print(tuple1[:-1])
