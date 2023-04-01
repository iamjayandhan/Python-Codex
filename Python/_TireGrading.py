n=int(input())
steel=[]
for x in range(n):
    steel.append(list(map(float,input().split())))
for item in steel:
    (condition1,condition2,condition3)=(False,False,False)
    if item[0]==50:
        condition1=True
    if item[1]==0.7:
        condition2=True
    if item[2]==5600:
        condition3=True
    elif condition1==True and condition2==True and condition3==True:
        Grade=10
    elif condition1==True and condition2==True:
        Grade=9
    elif condition2==True and condition3==True:
        Grade=8
    elif  condition1==True and condition3==True:
        Grade=7
    elif condition1==True or condition2==True or condition3==True:
        Grade=6
    elif condition1!=True and condition2!=True and condition3!=True:
        Grade=5
    print(Grade)