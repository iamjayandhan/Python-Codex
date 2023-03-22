n=int(input())
salary_list=[]
for i in range(n):
    salary_list.append(int(input()))
for salary in salary_list:
    if salary<1500:
        HRA=salary*10/100
        DA=salary*90/100
    elif salary>=1500:
        HRA=500
        DA=salary*98/100
    Gross_salary=salary+HRA+DA
    print(Gross_salary)
