x=[2.,'anwar',56,-234.5,False]
print('the original list is:',x)
x[0]=x[4]
for i in x:
    print(i)
print('length of the list is:',len(x))
del x[2]
print('after deleting x[2]:',x)
print('slicing of lists:',x[0:6])
print('new x[2] is :',x[2])
#negative index
print('x[-1],x[-3]:',x[-1],x[-3])