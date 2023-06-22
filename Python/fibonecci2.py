from time import sleep
n=int(input("Enter a number   :"))
def fib(n):
    a=0
    sleep(0.5)
    b=1
    sleep(0.5)
    print(a)
    sleep(0.5)
    print(b)
    
    for i in range(2,n):
        c=a+b
        a=b
        b=c
        print(c)
        sleep(0.5)
fib(n)