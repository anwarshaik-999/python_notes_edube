#observe the order and scope carefully
def func(list1):
    list1[0]=['list inside list']
    #here you are modifying the list1 which is pointing to ['anwar'] this is affected globally
    print('list1',list1)
    print('list2',list2)
list2=['anwar']
func(list2)
print(list2)
