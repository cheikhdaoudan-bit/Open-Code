"""🧪 Case 1 — student management
SWISS UMEF UNIVERSITY – Campus Dakar 
🟡 Statement
Create a program that :
1. ask :
• name
• 3 marks
2. Calculate the mean
3. Display :
• The mean
• The mention :
• ≥ 16 → Very Good
• ≥ 14 → Good
• ≥ 10 → Admitted
• < 10 → Fail"""

total=0
mention=""
count=1
name=input("Give me your name : ")
for i in range(3):
    mark=float(input(f"What's the mark number {count} of {name} ? : "))
    count+=1
    total+=mark
mean=total/3
if mean<10:
    mention="Fail"
elif mean>=10 and mean<14:
    mention="Admitted"
elif mean>=14 and mean<16:
    mention="Good"
else:
    mention="Very Good"
print(f"""----------------STUDENT RECORD----------------
The student {name} has the following performance :
-Mean={mean}
-Mention={mention}
    """)
