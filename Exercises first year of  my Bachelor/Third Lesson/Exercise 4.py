'''🟠 Case 4 (Class)
👉 Given marks : [12, 8, 15, 9, 10]
👉 Count how many student have a mark ≥ 10'''

mark_list=[12,8,15,9,10]
counter=0
for mark in mark_list:
    if mark>=10:
        counter+=1
print(f"The number of students with a mark greater than 10 or more is : {counter}")