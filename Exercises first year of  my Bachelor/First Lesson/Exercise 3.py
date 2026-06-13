"""🟠 Exercise 3 (University)
Enter 3 marks
👉 calculate the mean"""

count=1
total=0
for i in range(3):
    mark=float(input(f"Enter mark number {count} : "))
    count+=1
    total+=mark
mean=total/3
print(f"The mean of these marks is : {mean}")