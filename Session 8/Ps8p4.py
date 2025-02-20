def comp_rate(jcode):
    if jcode == "L":
        rate = 25
    elif jcode == "A":
        rate = 30
    else:
        rate = 50
    return rate

response = input("Would u like to run this program?").strip().lower()
total_gross = 0

while response == "yes":
    lname = input("Please enter last name: ").strip()
    jcode = input("Please enter job code: ").strip()
    hrs = float(input("Please enter hours worked: "))

    rate = comp_rate(jcode) 

    if hrs > 40:
        overtime = hrs - 40
        gross = (40 * rate) + (overtime * rate * 1.5)
    else:
        gross = hrs * rate

    print(f"Employee last name: {lname}")
    print(f"Gross pay: ${gross}")

    total_gross += gross

print(f"The sum of total gross pay: ${total_gross}")

