"""SWISS UMEF UNIVERSITY – Campus Dakar 
🟡 Exercise 2 (Mobile Money)
Contexte : money transfer
An user transfert money :
• if amount ≤ 10 000 → fee = 100
• else → 1%
👉 Calculate the total amount paid"""

fee=0
print("Welcome to the mobile money app")
amount=float(input("How much money would want you send ? : "))
if amount<=10000:
    fee=100
    total_amount=amount+fee
else:
    fee=1/100
    fee=amount*fee
    total_amount=amount+fee
print(f"The final amount to pay is {total_amount}")