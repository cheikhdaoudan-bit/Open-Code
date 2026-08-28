"""🎁 Bonus Challenge
Create a programm that :
• Input 5 amounts
• Use a function for :
• Calculate a reduction
• Calculate a tax
• Display the final total"""

def reduction(amounts):
    choice=input("The reduction is a number or a percentage ? : ")
    if choice.lower().strip()=="number":
        red=float(input("What's the reduction (number) that you will applied ? : "))
        new_amount=amounts-red
        return new_amount
    elif choice.lower().strip()=='percentage':
        percentage=float(input("What's the reduction (percentage) that you will applied ? : "))/100
        value_to_reduce=amounts*percentage
        new_amount=amounts-value_to_reduce
        return new_amount
    else:
        print("What did you want to say")
        return reduction(amounts)

def tax(amounts):
    choice=input("The tax is a number or a percentage ? : ")
    if choice.lower().strip()=="number":
        tax=float(input("What's the tax (number) that you will applied ? : "))
        new_amount=amounts+tax
        return new_amount
    elif choice.lower().strip()=='percentage':
        percentage=float(input("What's the tax (percentage) that you will applied ? : "))/100
        value_to_add=amounts*percentage
        new_amount=amounts+value_to_add
        return new_amount
    else:
        print("What did you want to say")
    return 0.0

#PROGRAMME PRINCIPALE

list_amount=[]
list_red=[]
list_tax=[]
total=0
total_red=0
total_tax=0
total_both=0
k=1
for i in range(5):
    amount=float(input(f"Enter the amount number {k}"))
    k+=1
    list_amount.append(amount)
    total+=amount
while True:
    choice=input("What's your choice ? (Reduction/Tax/Both) : ")
    match choice.lower().strip():
        case "reduction":
            for amount in list_amount:
                new_amount=reduction(amount)
                list_red.append(new_amount)
                total_red+=new_amount
            print(f"New amount = {list_red}")
            print(f"-Total after reduction={total_red}")
            list_red=[]
            total_red=0
        case "tax":
            for amount in list_amount:
                new_amount=tax(amount)
                list_tax.append(new_amount)
                total_tax+=new_amount
            print(f"New amount = {list_tax}")
            print(f"-Total after tax={total_tax}")
            list_tax=[]
            total_tax=0    
        case "both":
            for amount in list_amount:
                calculate_1=reduction(amount)
                calculate_2=tax(calculate_1)
                total_both+=calculate_2
                print(f"New amount = {calculate_2}")
            print(f"-Total after both = {total_both}")
            total_both=0
        case "quit":
            break
        case _:
            print("Explain again your demand, i don't understand")
