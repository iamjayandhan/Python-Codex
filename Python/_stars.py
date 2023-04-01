n=int(input())
for row in range(n,0,-1):
    for col in range(row,0,-1):
        if col!=1:
            print(".",end="")
        else:
            print("*",end=" ")
    print()
