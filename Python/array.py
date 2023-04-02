from array import *

arr=array('i',[])
n=int(input("Enter the length of the array :"))
for i in range(n):
    x=int(input("Enter the value :"))
    arr.append(x)
print(arr)
val=int(input("Enter the value for search "))
j=0

for k in arr:
    if k==val:
        print(j)
        break
    j+=1
else:
    print("Enter a valid number and try again....")
