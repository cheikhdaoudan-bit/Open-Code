'''SWISS UMEF UNIVERSITY – Campus Dakar
🟡 Exercise 1 (Market)
Contexte : Market
A customer enters the price of a product 
👉 Calculate the TTC price of the product (ATV)=18%
'''
ttc=18/100
print("What's the name of the product ? ")
name_product=input("")
print("Please to enter the price of the product : ")
price_product=float(input(""))
add_value=price_product*ttc
ttc_price=price_product+add_value
print(f"The ttc price of {name_product} is : {ttc_price}")