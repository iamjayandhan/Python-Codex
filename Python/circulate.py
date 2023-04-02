#8 Circulate n values
def circulate(alist):
    for i in range(len(alist)):
        a=alist.pop(0)
        alist.append(a)
        print(f"\t\tCirculate {i+1} : {alist}")
    return alist

def getvalues(n):
    nval=[]
    for i in range(n):
        v=input(f"Enter the Value {i+1} : ")
        nval.append(v)
    return nval

n=int(input("Enter the number of values wanted to be circulated >>> "))
list=getvalues(n)
print("\nGiven N Values : ", list)
print("\n","*"*15,"\tCirculate the N Value\t","*"*15,"\n")
circulate(list)