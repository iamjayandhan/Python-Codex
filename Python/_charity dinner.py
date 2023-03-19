pink=int(input())
green=int(input())
red=int(input())
orange=int(input())
amount=int(input())
ticket=[[o,r,g,p] for o in range(amount+1) 
        for r in range(amount+1) 
        for g in range(amount+1) 
        for p in range(amount+1) 
        if p*pink+g*green+r*red+o*orange==amount]

print("Total combination :",len(ticket))
if amount>0:
    print("Minimum number of tickets to print is 1")