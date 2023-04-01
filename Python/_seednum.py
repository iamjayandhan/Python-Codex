num=int(input())
seednum=int(input())

if num<0 or seednum<0:
    print("False")
elif (num)*((num%10)*2)*((num%100//10)*2)*((num%1000//100)*2)==seednum:
    print("True")
else:
    print("False")