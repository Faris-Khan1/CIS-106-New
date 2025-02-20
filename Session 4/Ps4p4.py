appl = input("Please enter name of appliance: ")
cost = float(input("Please enter cost of appliance: "))

if cost > 1000:
    warrantee = cost * 0.10
else:
    warrantee = cost * 0.05
total = cost + warrantee

print("Name: ", appl)
print("Cost: $", cost)
print("Warrantee: $", warrantee)
print("Total: $", total)
