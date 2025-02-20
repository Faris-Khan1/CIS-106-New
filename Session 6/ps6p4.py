response = input("Do you want to run this program? ")
total = 0
emp = 0

while response == "Yes":
    lname = input("Please enter last name: ")
    hrs = float(input("Please enter hours worked: "))
    rate = float(input("Please enter your hourly rate of pay: "))

    if hrs > 40:
        overtime = hrs - 40
        gross = (40 * rate) + (overtime * rate * 1.5)
    else:
        gross = hrs * rate

    emp = emp + 1
    total += gross

    print(f"Employee: {lname}, gross pay: {gross}")
    response = input("Do u want to enter another employee?")

if emp > 0:
    avg = total / emp
    print(f"total gross pay: ${total}")
    print(f"total number of employees: {emp}")
    print(f"Average pay of employees: ${avg}")
else:
    print(f"No employees were entered")

