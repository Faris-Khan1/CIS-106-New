total = 0
tax = 0

def compute_total(qty, unitp):
    global total
    total = qty * unitp 
    global tax
    tax = total * 0.07 

qty = int(input("Enter quantity of the item: "))
unitp = float(input("Enter unit price: "))

compute_total(qty, unitp)

print(f"Total: ${total}")
print(f"Tax: ${tax}")

