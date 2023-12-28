dict={'key1':'value1','key2':'value2','key3':{'key3.1':'value3.1','key3.2':'value3.2'}}
y=dict.items()
print(type(y))
print(y)
for i,j in y:
    print(i,'->',j)