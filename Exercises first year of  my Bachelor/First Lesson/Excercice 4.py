"""🟠 Exercice 4 (Class - loop)
Enter 5 marks
👉 calculate the sum"""


total=0
count=1
for i in range(5):
    mark=float(input(f"Enter mark {count} : "))
    total+=mark
    count+=1
print(f"the sum of all of marks is : {total}")