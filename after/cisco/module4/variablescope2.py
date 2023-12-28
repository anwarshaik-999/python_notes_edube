def scope_test():
    x = 123
x=9
scope_test()
print(x)
#the function unable to change the variable value
#by using global we can do it
def scope_test2():
    global y
    y = 123
y=10
scope_test2()
print(y)

