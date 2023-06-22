def check_for_duplicates(stg):
    c=0
    for ch in stg:
        if ch==" ":
            stg[stg.index(ch)]=""
        else:
            c += stg.count(ch)-1
            stg[stg.index(ch)]=""
    if c==0:
        return (0)
    return (c)
s = list(input("enter the string  :").strip())
print(check_for_duplicates(s))