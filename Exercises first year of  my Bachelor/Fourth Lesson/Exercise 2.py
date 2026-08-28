"""🟡 Exercise 2
Make a function result(mark) that displays :
• "Admitted" if mark ≥ 10
• "Failed" else"""

def result(mark):
    if mark >= 10:
        print(f'With a mark of {mark} , this student is admitted')
    else: 
        print(f"With a mark of {mark} , this student failed")