len=int(input())
bre=int(input())

area=len*bre
per=2*(len+bre)

if area>per:
    print("Area")
    print(area)
elif area<per:
    print("Peri")
    print(per)
else:
    print("Eq")