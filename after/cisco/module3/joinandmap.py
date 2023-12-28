array=['anwar',19,'shaik',65.324,True]
array2=['a','b','c']
print(map(str,array))
print(list(map(str,array)))
print(type(map(str,array)))
print(type(array))
print(array)
print(''.join(map(str,array)))
print(map(str,array2))
#map(str,array) will not perform any work but it will just returns an object 
#list(map(str,array)) it will perform an operation