dic={ 'key2':'value2',
    'key3':'value3',
    'key1':'value1',
   
    'key4':{
        "key4.1":'value4.1',
        'key4.2':'value4.2'
    }
}
for i in dic:
    print(type(i))
    print(i)
print(dic.items())
for i in dic.items():
    print(type(i))
    print(i)