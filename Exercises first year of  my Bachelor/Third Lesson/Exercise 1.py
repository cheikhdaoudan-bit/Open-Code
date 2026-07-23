"""🟡 Case 1 (University)
👉 Input 5 marks
👉 Store them in a list
👉 Calculate the mean"""

total_marks=0
mark_list=[]
for i in range(5):
    mark= float(input("Enter a mark of a student : "))
    total_marks+=mark
    mark_list.append(mark)
mean=total_marks/5
print(f"The marks of students are here : ---{mark_list}--- and the mean is : {mean}")