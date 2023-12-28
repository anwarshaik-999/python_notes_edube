import time
for i in range(5):
    print(i+1,'Mississippi')
    time.sleep(1)
    #similar to settimeout here it takes 1 sec but executes synchronously
print('Ready or not, here I come!')