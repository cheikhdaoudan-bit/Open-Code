"""SWISS UMEF UNIVERSITY – Campus Dakar
🧪 Case 3 — Mobile Money
🟠 Statement
An user do many transferts :
• 3 operations
• Fees :
• If ≤ 10 000 → 100
• Else → 1%
👉 Display :
• Total send
• Fees total"""

fees_total=0
total_money=0
for i in range(3):
    amount=int(input('How much money want you send : ?'))
    if amount<=10000:
        fee=100
        fees_total+=fee
        total_money+=amount
    else: 
        fee=amount*0.01
        fees_total+=fee
        total_money+=amount
print(f"The total send by the user is : {total_money} and the fees total is {fees_total}")