"""🧪 Case 2 — Trade (Market)
SWISS UMEF UNIVERSITY – Campus Dakar
🟡 Statement
A trader calculate the final price :
• Price entered
• If ≥ 20 000 → reduction 15%
• Else → reduction 5%
• VAT = 18%
👉 Display the final price"""

reduction=0
VAT=18/100
price=float(input("Input the price of the product : "))
if price>=20000:
    reduction=15/100
else:
    reduction=5/100
value_reduced=price*reduction
price_reduced=price-value_reduced
value_added=price_reduced*VAT
final_price=value_added+price_reduced
print(f"The final price of the product is {final_price}")