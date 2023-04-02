camel = input("Enter a string : ")
for i in camel:
    if i.isupper():
        print(i.replace(i,("_"+i.lower())),end="")
    else:
        print(i,end="")
