response = input("Do u want to run this program?")
total_disc = 0

while response == "Yes":
    qty = float(input("Please enter the quantity of the item: "))
    price = float(input("Please enter price of the item: "))
    ext_price = qty * price

    if ext_price > 10000:
        disc = ext_price * 0.25
    else: 
        disc = ext_price * 0.10
    total = ext_price - disc

    print(f"extended price: ${ext_price}")
    print(f"discount amount: ${disc}")
    print(f"total: ${total}")

    total_disc += disc
    response = input("Would u like to rerun this program?")

print(f"Sum of all discounts: ${total_disc}")
