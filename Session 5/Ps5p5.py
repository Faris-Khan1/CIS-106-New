lname = input("Please enter last name: ")
salary = float(input("Please enter salary: "))
lvl = float(input("Please enter job level: "))

if lvl >= 10:
    rate = 0.25
elif lvl >= 5:
    rate = 0.20
else: 
    rate = 0.10

bonus = rate * salary

print(f"Last name: {lname}")
print(f"bonus: ${bonus}")
