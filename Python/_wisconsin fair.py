salary=int(input("Enter the total salary paid : "))
weekend=(salary - 80*10)/130
weekday=10+int(weekend)
print("Number of weekday hours is",weekday)
print("Number of weekend hours is",int(weekend))