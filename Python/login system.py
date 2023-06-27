# Coding a login system in python
# difficulty = easy/moderate

#user inputs
action=input('to log in, type "login". to create an account, type "create". and to delete an account, type "delete". ')

# functions
def create_account(file="username + passwords.txt"):
    username=input('username :')
    password=input('password :')

    with open(file, 'a') as myFile:                                             # 'a' means to add text
        myFile.write(encrypt(username) + ',' + encrypt(password) + '\n')        # encrypt function used below

def delete_account(file="usernames + passwords.txt"):
    account=input('which account would you like to delete? ')
    password=input("please verify your account's password :")

    with open(file, 'r') as myFile:                                             # 'r' means read
        text=myFile.read()

    text=text.replace(encrypt(account) + ',' + encrypt(password), '')

    with open(file, 'w') as myFile:                                             # 'w' means to write over the whole text file
        myFile.write(text)

def login(file='usernames + passwords.txt'):
    account=input('username :')
    password=input('password :')

    with open(file, 'r') as myFile:
        text=myFile.read()                                                      # changinf the text into a variable
    
    find_account=text.find(encrypt(account) + ',' + encrypt(password) + '\n')   # the '\n' makes sure that there is a new line after the text

    if find_account !=-1:
        print('Welcome, ' +account)                # if the accountis found, the output is 0, else, it is -1
    else:
        print('no such user or incorrect password')   


def encrypt(string):
    encrypted=''

    for char in string:          # will cycle through every character in the string
        if char!='r' or char!='t':
            encrypted+=chr(ord(char) + 1)       # shift by 1
        elif char=='r':
            encrypted+='a'
        elif char=='t':
            encrypted+='t'

    return encrypted

# run correct functions
if action=='create':
    create_account()
if action=='delete':
    delete_account()
if action=='login':
    login()
