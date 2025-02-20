qty = float(input("Please enter quantity of an item: "))

if qty >= 1000:
    unitp = 3
else:
    unitp = 5
ext_price = qty * unitp
tax = ext_price * 0.07
total = ext_price + tax

print("Quantity: ", qty)
print("Unit price: $", unitp)
print("Extended price: $", ext_price)
print("Tax: $", tax)
print("Total: $", total)


