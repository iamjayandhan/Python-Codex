n=int(input())
L1=[0] *n
L2=[0]*n
for i in range(n):
    L2[i]=int(input())
for i in range(n):
    L1[i]=int(input())
    
for i in range(n):
    L2[i]=L2[i]-L1[i]

L2.sort()
su=0
ans=0
for i in range(n):
    su=su+L2[i]
    if su<0:
        ans = ans + abs(su)
        su=0
        
print(ans)