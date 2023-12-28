dic={ 'key2':'value2',
    'key3':'value3',
    'key1':'value1',
   
    'key4':{
        "key4.1":'value4.1',
        'key4.2':'value4.2'
    }
}
dic2=dic.copy()
dic3=dic.clear()
print(dic2)
print(type(dic2.clear()))
print(dic2)
print(dic3)
print(dic)
