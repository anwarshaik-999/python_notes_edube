#observe the order and scope carefully
def func(list1):
    del list1[0]
    # list1 is accessing the list coz it acts like a pointer
    print('list2',list2)
list2=['anwar']
func(list2)
print(list2)
