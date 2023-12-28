x=10
y=x
x=11
print(y)
list1=[1]
list2=list3=list1
#the above list 2,3 stores the address of the list1
list1=[2]
print(list2,list3)
list3[0]='anwar'
print(list2,list3)