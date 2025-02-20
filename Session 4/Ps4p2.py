item = input("Please enter item A or B: ")
qty = float(input("Please enter quantity: "))

if item == "A":
    unitp = 20
else:
    unitp = 10
ext_price = unitp * qty

print("Item: ", item)
print("Unit price: $", unitp)
print("Extended price: $", ext_price)
