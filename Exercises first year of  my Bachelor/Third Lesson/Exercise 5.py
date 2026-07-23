""" Case 5 (Simple Analysis)
👉 Get 5 students marks's
👉 Display :
• The mean
• Number of admitted (mark ≥ 10)"""

total=0
mark_list=[]
counter=0
for i in range(5):
    mark=float(input('Enter the mark you want to store : '))
    if mark>=10:
        counter+=1
    mark_list.append(mark)
    total=sum(mark_list)
mean=total/5
print(f"""-The mean of the class = {mean}
-The number of admitted = {counter}
""")