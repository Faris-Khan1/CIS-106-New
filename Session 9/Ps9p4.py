def compute_ticket_price(miles):
    if miles >= 30:
        price = 12
    elif miles >= 20:
        price = 10
    elif miles >= 10:
        price = 8
    else:
        price = 5
    return price  

response = input("Would you like to run this program?").strip().lower()
total_price = 0  

while response == "yes":
    lname = input("Please enter last name: ").strip()
    miles = float(input("Please enter miles from downtown Chicago: "))

    ticket_price = compute_ticket_price(miles)

    total_price += ticket_price

    print(f"Last Name: {lname}")
    print(f"Miles from downtown Chicago: {miles}")
    print(f"Ticket Price: ${ticket_price}")

    response = input("Would you like to run this program again? ").strip().lower()

print(f"\nTotal price of all tickets: ${total_price}")
print("End of program.")
