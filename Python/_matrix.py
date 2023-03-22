from numpy import *
import numpy

arr=matrix('1 2 3;4 5 6;7 8 9')
print(arr)
print("\n")

m=numpy.delete(arr,0,0)
print(m)
print("\n")

m=numpy.delete(arr,1,1)
print(m)
print("\n")

m=numpy.delete(arr,0,1)
print(m)
print("\n")


