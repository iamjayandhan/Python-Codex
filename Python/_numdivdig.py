num=int(input()) 

if num<=0: 
    print("invaild input")
else:
    numcopy=num;sum=0;i=1
    while num:
        sum=sum + num%10
        if i==len(str(num)): 
            break
        else: 
            i=i+1
            num=num//10
    print("True" if numcopy%sum==0 else "False")
