cents=[5,10,25]
amt_due=int(input("Amount Due: "))
for i in range(amt_due):
    coin=int(input("Insert Coin: "))
    if coin in cents:
        amt_due=amt_due-coin
        print("Amount Due: ",amt_due)
        if amt_due==0:
            break
    else:
        pass