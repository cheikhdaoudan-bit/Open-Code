"""🧪 Case 4 — Class Management 
🔴 Statement
For 5 students :
• Input marks
• Calculate mean of the class
• Count how many have mean >= 10
"""


total_marks=0
counter=0
for i in range (5):
    marks=float(input("Enter the mark of the student : "))
    total_mean+=marks
    if marks>=10:
        counter+=1
mean=total_mean/5

print(f"This class have {mean} for mean and we have {counter} students who have a mean >= 10")