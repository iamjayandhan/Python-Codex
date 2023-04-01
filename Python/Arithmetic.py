"""Arithmetic operators :
+,-,*,/,//,%,**  """

def add(a,b):
    return (a+b)
def subtract(a,b):
    return (a-b)
def product(a,b):
    return (a*b)
def floordivision(a,b):
    return (a//b)
def floatdivision(a,b):
    return (a/b)
def modulus(a,b):
    return (a%b)
def power(a,b):
    return(a**b)

print("""ARITHMETIC OPERATORS
1.add
2.subtract
3.product
4.floordivision
5.float division
6.modulus
7.power""")

a=int(input("enter the number 1: ")) 
b=int(input("enter the number 2: "))
op=int(input("enter the option for the arithmetic operation : "))

while op in [1,2,3,4,5,6,7]:
    if op==1:
        print()
        print("the answer is ",add(a,b))
    if op==2:
        print()
        print("the answer is ",subtract(a,b))
    if op==3:
        print()
        print("the answer is ",product(a,b))
    if op==4:
        print()
        print("the answer is ",floordivision(a,b))
    if op==5:
        print()
        print("the answer is ",floatdivision(a,b))
    if op==6:
        print()
        print("the answer is ",modulus(a,b))
        print()
    if op==7:
        print("the answer is ",power(a,b))
    if op==0 :
        print("Thank You")
    
    print()
    print("""If you need to perform any other operation then enter the option else enter 0

    ARITHMETIC OPERATORS
    0.EXIT
    1.add
    2.subtract
    3.product
    4.floordivision
    5.float division
    6.modulus
    7.power
    """)
    
    op=int(input("enter the option : "))