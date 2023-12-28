#dictionaries are mutable unlike tuples
print()
print('updating values')
dict={'key1':'value1','key2':'value2','key3':{'key3.1':'value3.1','key3.2':'value3.2'}}
print('before:',dict)
dict['key1']=1
print(dict)
print()
print('adding new items')
dict['newkey']='newvalue'
print(dict)
print()
print('adding new items with update')
dict.update({'key2':2.200})
print(dict)
print()
print('deleting items')
del dict['key3']['key3.2']
print(dict)
print()
print('poping the last item')
dict.popitem()
print(dict)