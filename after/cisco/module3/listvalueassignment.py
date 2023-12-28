list1=['anwar',34,True]
list2=list1[:]
list1[1]='xyz'
print(list2)
list2=list1[0:-1]
print(list2)