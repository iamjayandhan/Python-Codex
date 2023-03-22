N=int(input())
people=[]
house=[]

for i in range(N):
    people.append(int(input()))
for j in range(N):
    house.append(int(input()))

got=0
for i in range(N):
    for j in range(N):
        if (people[i]<house[j]):
            got+=1
            house[j]=-1
            break
        
print(N-got)   

