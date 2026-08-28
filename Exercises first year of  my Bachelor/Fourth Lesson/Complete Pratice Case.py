"""🧩 Cas pratique complet - Boutique de téléphones
Le programme doit :
• input 5 purchases
• Calculate the reductions
• Calculate fees of deliveries
• Display the final total
Réduction :
• Amount ≥ 20 000 → 10%
• Else → 5%
Delivery :
• Less than 30 000 → 2 000 FCFA
• Else → free
👉 Create reduction (amount) and delivery(amount), then write the principal programm."""

def reduction(amounts):
    if amounts>=20000:
        reduction=0.1
        new_amount=amounts*reduction
        final_amount=amounts-new_amount
    else:
        reduction=0.05
        new_amount=amounts*reduction
        final_amount=amounts-new_amount
    return reduction,final_amount

def fees_deliveries(amounts):
    if amounts<30000:
        fee_delivery=2000
        final_amount=amounts+fee_delivery
    else:
        fee_delivery=0
        final_amount=amounts
    return fee_delivery,final_amount
#PROGRAMME PRINCIPAL
amount_list=[]
for i in range(5):
    amount=float(input("Enter the amount that you send : "))
    amount_list.append(amount)
while True:
    choice=input("What's your choice ? : ")
    match choice.lower():
        case 'reduction':
            for amount in amount_list:
                calculate_1,final_amount_reduction=reduction(amount)
                print(f"The amount that you should pay is : {final_amount_reduction}")
        case "delivery":
            for amount in amount_list:
                calculate_2,final_amount_delivery=fees_deliveries(amount)
                print(f"The amount that you should pay is : {final_amount_delivery}")
        case 'both':
            total=0
            for amount in amount_list:
                calculate_1,final_amount_reduction=reduction(amount)
                calculate_2,final_amount_delivery=fees_deliveries(final_amount_reduction)
                print(final_amount_delivery)
                total+=final_amount_delivery
            print(f"The total = {total}")
        case "quit":
            print("Thank to you to have used money cash system")
            break
        case _:
            print("Explain again your demand, i don't understand")
            