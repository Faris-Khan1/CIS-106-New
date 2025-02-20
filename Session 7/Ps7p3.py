f = open("employees.txt", "r")
total_bonus = 0

lname = f.readline().strip()
while lname != "":
    salary = f.readline().strip()
    salary = float(salary)

    if salary >= 100000:
        rate = 0.20
    elif salary >= 50000:
        rate = 0.15
    else:
        rate = 0.10

    bonus = salary * rate

    print(f"Employee Last Name: {lname}, Salary: ${salary}, Bonus: ${bonus}")

    total_bonus += bonus 
    lname = f.readline().strip()

f.close()

print(f"Total bonuses paid out: ${total_bonus}")
