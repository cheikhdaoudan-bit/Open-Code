"""🟠 Case 3 (Shop)
👉 Given the price list : [1000, 2500, 3000, 1500]
👉 Find the highest price"""

price_list=[1000,2500,3000,1500]
price_max=price_list[0]
for price in price_list:
    if price_max<=price:
        price_max=price
print(f"The hightest price is : {price_max} ")
