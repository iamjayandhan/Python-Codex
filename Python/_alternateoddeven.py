x,y,z=map(int,input().split())
if x%2==0 and y%2!=0 and z%2==0:
    print(x,y,z)
elif x%2==0 and y%2==0 and z!=0:
    print(x,z,y)
elif x%2!=0 and y%2==0 and z%2==0:
    print(y,x,z)

elif x%2!=0 and y%2!=0 and z%2==0:
    print(x,z,y)
elif x%2!=0 and y%2==0 and z%2!=0:
    print(x,y,z)
elif x%2==0 and y%2!=0 and z%2!=0:
    print(y,x,z)