import sys
users={}
status=""

print("Hacking Academy 2021")
def displayMenu():
    status=input("Are you registered user? y/n? press q to quit :")
    if status=="y":
        oldUser()
    elif status=="n":
        newUser()
    else:
        exit()

def newUser():
    createLogin=input("Create login name :")
    if createLogin in users:
        print("\nLogin name already exist!\n")
    else:
        createPassw=input("Create password :")
        users[createLogin]=createPassw
        print("\nUser created\n")

def oldUser():
    login=input("Enter login name :")
    passw=input("Enter password :")
    
    if login in users and users[login]==passw:
        print("\nLogin successful!")
    else:
        print("\nUser doesn't exist or wrong password!\n")

while status!="q":
    displayMenu()
