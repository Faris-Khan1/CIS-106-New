part = float(input("Please enter part number: "))
qty = float(input("Please enter quantity of parts: "))

if part == 10 or part == 55:
    cost = 1
elif part == 99:
    cost = 2
elif part == 80 or part == 70:
    cost = 3
else:
    cost = 5
total = qty * cost

print(f"part number: {part}")
print(f"cost per unit: ${cost}")
print(f"total: ${total}")
