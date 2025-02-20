f = open("Data1.txt", "r")
total_ext = 0
count = 0

item = f.readline().strip()
while item != "":
    qty = f.readline().strip()
    qty = float(qty)
    price = f.readline().strip()
    price = float(price)

    ext_price = qty * price 

    print(f"Item: {item}, Quantity: {qty}, Price: ${price}, Extended Price: ${ext_price}")

    total_ext += ext_price
    count += 1

    item = f.readline().strip()

f.close()

if count > 0:
    avg = total_ext / count
else:
    avg = 0

print(f"Total of all extended prices: ${total_ext}")
print(f"Total number of orders: {count}")
print(f"Average order total: ${avg}")


