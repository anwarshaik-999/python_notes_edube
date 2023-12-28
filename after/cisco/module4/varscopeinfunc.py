#observe the order and scope carefully
def func(list1):
    list1=['anwarshaik']
    print('list1',list1)
    print('list2',list2)
    list2=[1,2,3]
    # here you might think first list2 is global and second is local but it's not how it works as i said before  entire function is treated as single line so it will consider all the lines as single line and the reason for error same after words
list2=['anwar']
func(list2)
print(list2)
