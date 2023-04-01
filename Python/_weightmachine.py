def WeightMachine(N,T,weights):
    payable=0
    for weight in range(1,N+1):
        get=int(input("Weight {}: ".format(weight)))
        weights.append(get)
    for item in weights:
        if item<=T:
            payable+=1
        elif item>T:
            payable+=2
    return payable

N=int(input("Number of Weights: "))
T=int(input("Threshold Weight: "))
weights=[]
print("Payable: ${}".format(WeightMachine(N,T,weights)))