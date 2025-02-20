qty = float(input("Please enter number of concert tickets: "))

if qty >= 25:
    price = 50
elif qty >= 10 and qty <= 24:
    price = 60
elif qty >= 5 and qty <= 9:
    price = 70
elif qty < 5:
    price = 75
total = qty * price

print(f"Number of tickets: {qty}")
print(f"Price of ticket: ${price}")
print(f"Total: ${total}")
