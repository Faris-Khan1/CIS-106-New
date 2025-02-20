lname = input("Please enter last name: ")
depend = float(input("Please enter number of dependents: "))
gross = float(input("Please enter gross income: "))

adjusted = gross - (depend * 12000)
if adjusted > 50000:
    rate = 0.20
else:
    rate = 0.10
tax = rate * adjusted
if tax < 0:
    tax = 100

print("Last name: ", lname)
print("Gross income: $", gross)
print("dependents: ", depend)
print("Adjusted gross income: $", adjusted)
print("Income tax: $", tax)
