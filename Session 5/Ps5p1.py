qty = float(input("Please input quantity of widgets: "))

if qty > 10000:
    price = 10
elif qty <= 10000 and qty >= 5000:
    price = 20
else:
    price = 30
ext_price = qty * price
tax = ext_price * 0.07
total = ext_price + tax 

print(f"Extended price: ${ext_price}")
print(f"Tax: ${tax}")
print(f"Total: ${total}")
