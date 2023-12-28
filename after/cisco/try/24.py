#for i in range(100):((i-2)%6==0 or i%6==0) and print(i)
j=0
for i in range(0,100,2):
    if not j%4:
        print(i)
        print(i+2)
    j+=1