print('normal starting')
try:
    print('before error')
    print(0/0)
    print('after error')
#print('middle')
except:
    print('unexpected error')
print('normal ending')