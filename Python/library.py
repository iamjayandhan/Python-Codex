#12 Items in library
print("_"*50)
print("\n"," "*10,"KGiSL Library Management System")
print("_"*50)

BooksCatelogue=["PSPP","Mathamathics","English","Physics","Chemistry"]
IssuedBook=[]

choice=int(input(('''
1.Add Book
2.Delete Book
3.View Book list
4.Issue Book
5.Return Book
Enter the choice : ''')))

while choice:
    if choice==1:
        print("#"*20)
        print(" "*5,"Add Book")
        print("#"*20)
        BookName=input("Enter Book Name : ")
        BooksCatelogue.append(BookName)
    if choice==2:
        print("#"*20)
        print(" "*5,"Delete Book")
        print("#"*20)
        BookName=input("Enter Book Name : ")
        BooksCatelogue.remove(BookName)
    if choice==3:
        print("#"*40)
        print(" "*7,"Available Book List")
        print("#"*40)
        for sno,book in enumerate(BooksCatelogue,start=1):
            print(sno,"-",book,"-",BooksCatelogue.count(book),"Available")
    if choice==4:
        print("#"*20)
        print(" "*5,"Issue Book")
        print("#"*20)
        BookName=input("Enter Book Name : ")
        IssuedBook.append(BookName)
        BooksCatelogue.remove(BookName)
    if choice==5:
        print("#"*20)
        print(" "*5,"Return Book")
        print("#"*20)
        BookName=input("Enter Book Name : ")
        BookID=IssuedBook.index(BookName)
        BooksCatelogue.append(IssuedBook.pop(BookID))

    print("_"*50)
    print("\n"," "*10," KGiSL Library Management System")
    print("_"*50)
        
    choice=int(input('''
    1.Add Book
    2.Delete Book
    3.View Book list
    4.Issue Book
    5.Return Book
    0.EXIt
    Enter the choice : '''))
