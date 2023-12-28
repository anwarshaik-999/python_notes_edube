for i in range(int(input())):
    x=list(map(lambda x:int(x),input().split()))
    if x[0]>x[1]*10:
        print('yes')
    else:print('no')