""" Case 2 (Mobile Money)
👉 Input many amounts
👉 Store them in a list
👉 Calculate the total"""

total=0
amount_list=[]
n=int(input("How many amounts do you want to enter ? : "))
for i in range(n):
    amount=float(input('How much money do you want to send ? : '))
    total+=amount
    amount_list.append(amount)

print(f"""-Total ={total}
-Here is the list of your amounts : {amount_list} """)