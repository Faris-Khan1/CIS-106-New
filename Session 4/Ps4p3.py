books = float(input("Please enter number of books: "))
cost = float(input("Please enter cost per book: "))

total = books * cost
if total >= 50:
    shipping = 25
else:
    shipping = 0

print("Order total: $", total)
print("Shipping fee: $", shipping)
