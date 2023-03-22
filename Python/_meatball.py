n=int(input())
m=0
mxPos=0
v=[0]*n
x=int(input())
for i in range(n):
    v[i]=int(input())

for i in range(n):
    v[i]=(v[i]-1)//x
for i in range(n):
    if v[i]>=m:
        m=v[i]
        mxPos=i

print(mxPos+1)