dic1={'key1':'value1','key2':{'key2.1':'value2.1','key2.2':'value2.2'}}
print(dic1,len(dic1))
emptydic={}
print(emptydic)
x=dic1.keys()
print(type(x))
print(x)
print(type(dic1['key1']))
# dic1['key1']+=(19,)
#error because the  value of the key used is not a tuple
# print(dic1['key1'])
# print(type(dic1['key1']))
k='key1'
dic2={
    k:'val'
}
print(dic2)