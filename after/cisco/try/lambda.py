import time
print(list(map(lambda x:x*2,range(10))))
print(type(range(10)))
print(type(time.sleep(1)))
#in map(x,y) it takes y and convert to x and returns
print(list(map(lambda x: not time.sleep(0.5) and x,range(10))))
#if you remove list() the map will simply return an object without performing any thing
print(list(map(lambda x:time.sleep(1) and x,range(10))))