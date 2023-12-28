dic={ 'key2':'value2',
    'key3':'value3',
    'key1':'value1',
    'key4':{
        "key4.1":'value4.1',
        'key4.2':'value4.2'
    }
}
print(dic['key3'])
print(dic['key4']['key4.1'])
print(dic.keys())
print(type(dic.keys()))
print(sorted(dic.keys()))
print(type(sorted(dic.keys())))
for i in dic.keys():
    print(dic[i])