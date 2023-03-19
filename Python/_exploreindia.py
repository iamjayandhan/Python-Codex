import math
n=int(input())-1
m=int(input())-1
x=int(input())-1
y=int(input())-1

ans=math.factorial(n+m)
ans=ans//(math.factorial(n))
ans=ans//(math.factorial(m))

ans1=math.factorial(x+y)
ans1=ans1//(math.factorial(x))
ans1=ans1//(math.factorial(y))

x1=n-x
y1=m-y

ans2=math.factorial(x1+y1)
ans2=ans2//(math.factorial(x1))
ans2=ans2//(math.factorial(y1))
print(ans-(ans1*ans2))