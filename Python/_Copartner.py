copartners=[[3,6,"UB"],[2,5,"MB"],[1,4,"LB"],[7,8,"SL"]]
n=int(input())
for p in copartners:
    index=not(p.index(n))
    print(p[index],p[-1])