for i in range(5):
    print(i)
else:print(i)
print()
# 0 to 4
for i in range(5):
    print('before:',i)
    i+=2
    print('after',i)
else:print(i)
#0 to 4 and then 6 
# the value of i we change inside the for loop has no impact it will again change its value while iterating
#observe the difference