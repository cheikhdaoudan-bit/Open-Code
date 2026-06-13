"""SWISS UMEF UNIVERSITY – Campus Dakar 
🔴 Exercise 5 (Challenge)
Count how many students have a mark >=10 (among 5 students)"""

count=1
count_mean=0
for i in range(5):
    mark=float(input(f"Enter mark number {count} : "))
    count+=1
    if mark>=10:
        count_mean+=1
print(f"The number of students have a mark more than or equal to 10 is : {count_mean}")