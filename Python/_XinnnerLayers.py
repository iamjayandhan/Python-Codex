from numpy import *
import numpy 

r,c =input().split(" ")
r=int(r)
c=int(c)
mat=[[0 for i in range(c)]for j in range(r)]
#val=1
for i in range(r):
  for j in range(c): 
      a=int(input())
      mat[i][j]=a
m=matrix(mat)
print(m)
q=m
#q=numpy.delete(q,0,0)
q=numpy.delete(q,0,0)
q=numpy.delete(q,0,1)
print(q)