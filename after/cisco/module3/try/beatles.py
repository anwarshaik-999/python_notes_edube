# step 1
beatles=[]
print("Step 1:", beatles)
for i in range(4):
    beatles.append(input())
# step 2
print("Step 2:", beatles)
for i in range(2):
    beatles.append(input())
# step 3
print("Step 3:", beatles)
del beatles[-1]
del beatles[-1]
# step 4
print("Step 4:", beatles)
beatles.insert(0,'Ringo starr')
# step 5
print("Step 5:", beatles)
# testing list length
print("The Fab", len(beatles))