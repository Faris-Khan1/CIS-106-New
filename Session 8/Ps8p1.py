def comptotal(qty, price):
    total = float(qty) * float(price)

    if total > 10000:
        total = total * 0.90
    else:
        total = total
    
    return total

ext_price = 0

response = input("Would u like to run this program?")

while response == "Yes":
    qty = float(input("Please enter Quantity: "))
    price = float(input("Please enter price: "))

    total = comptotal(qty, price)

    print(f"Total: ${total}")

    ext_price += total
    response = input("Would u like to rerun this program?")

print(f"Total extended price: ${ext_price}")
