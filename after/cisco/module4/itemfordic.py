dic={ 'key2':'value2',
    'key3':'value3',
    'key1':'value1',
    'key4':{
        "key4.1":'value4.1',
        'key4.2':'value4.2'
    }
}
dic2={  'key2':'value2',
    'k':'value3',
}
#below i confused that what is i and i forgot to see that for is iterating on tuple
for i in (dic,dic2):
    print(type(i))
    print(i)