"""🧩 Real Case : "Dakar Dem Dikk"
Create a function transportation_price(distance) with given rules :
• If distance < 5 km → 200 FCFA
• Else → 500 FCFA"""

def transportation_price(distance):
    if distance<5:
        price=200
    else:
        price=500
    print(f"The price of the journey is : {price}")
