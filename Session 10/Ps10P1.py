def compute_discount(qty, price, disc_rate):
    disc_amount = price * disc_rate
    disc_price = price - disc_amount
    return disc_amount, disc_price

qty = int(input("Enter the quantity: "))
price = float(input("Enter the price per item: "))
disc_rate = float(input("Enter the discount rate "))

disc_amount, disc_price = compute_discount(qty, price, disc_rate)

print(f"Quantity: {qty}")
print(f"Price per item: ${price}")
print(f"Discount Amount: ${disc_amount}")
print(f"Discounted Price: ${disc_price}")

