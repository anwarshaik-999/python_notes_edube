board=[["| |" for i in range(8)] for i in range(8)]
for j in range(8):
        print(" _ ",end="")
for i in range(8):
    print()
    for j in range(8):
        print(board[i][j],end="")
    print()
    for j in range(8):
        print(" _ ",end="")
