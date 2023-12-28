var = -0b110
print(type(var))
var_right = var >> 2
var_left = var << 2
print( var_left,var, var_right)
print('bin->', bin(var))
# str1='0b'+'11'
# str1=bin(str1)
var=bin(var)
print(var,type(var))
var=int(var,2)
print(var)
