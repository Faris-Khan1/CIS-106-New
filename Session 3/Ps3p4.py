make = input("Please enter make of the car: ")
model = input("Please enter model of the car: ")
msrp = float(input("Please enter msrp amount: "))
disc_perc = float(input("Please enter discount percent in decimal: "))

amt_off = msrp * disc_perc
disc_price = msrp - amt_off

print("Make: ", make)
print("Model: ", model)
print("MSRP: $", msrp)
print("Discount percent: ", disc_perc)
print("Discount amount: $", amt_off)
print("Discounted price: $", disc_price)
