from time import *
import sys

a=input("First name? ")
b=input("Middle name? [OPTIONAL]")
c=input("Sur/Last name? ")
s=input("Are you junior?[y/n] ")
if s=="y":
    s="Jr"
elif s=="n":
    s="Sr"
else:
    print("Your FULL name is : ",a,b,c)
    exit()
print("Your FULL name is : ",a,b,c,s)
        

        