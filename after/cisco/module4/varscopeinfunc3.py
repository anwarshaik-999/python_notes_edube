#observe the order and scope carefully
def func(list1):
    print('list1',list1)
    print('list2',list2)
    #here list2 is accessed globally before it conclude like this it will first check whether any list2 is declared with in the function whether top of it or bottom of it because function acts as a single line of instruction for the interpreter
list2=['anwar']
func(list2)
print(list2)
