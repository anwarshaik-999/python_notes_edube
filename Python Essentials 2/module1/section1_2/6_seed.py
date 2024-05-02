from random import random,seed
for i in range(3):
    print(random())
#we will get different values for every execution
seed(1)#by default seed sets with current time
for i in range(3):
    print(random())
'''
0.13436424411240122
0.8474337369372327
0.763774618976614
'''
#same o/p for every execution as we fixed the seed value
#the values depend on seed value