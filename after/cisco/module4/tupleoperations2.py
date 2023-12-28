tuple1=('tuple1',)
tuple2=('tuple2',)
tuple3=('tuple3',)
tuple1,tuple2,tuple3=tuple3,tuple2,tuple1
print(tuple1,tuple2,tuple3)
newtuple=tuple2+(100,)
newtuple2=tuple2*3
print(newtuple,newtuple2)
print('tuple2'in tuple2)
print('tuple2' in newtuple)
print('tuple2' in newtuple2)