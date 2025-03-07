def compute_price(msrp, make, model, ev):
    disc = 0  

    if make == "honda" and model == "accord":
        disc = 0.10
    elif make == "toyota" and model == "rav4":
        disc = 0.15
    elif ev == "yes":  
        disc = 0.30
    else:
        disc = 0.05  

    disc_price = msrp * (1 - disc)

    final_price = disc_price * 1.07

    return final_price  

response = input("Would you like to run this program? ").strip().lower()
total_msrp = 0
total_sales_price = 0

while response == "yes":
    make = input("Enter the make of the vehicle: ").strip()
    model = input("Enter the model of the vehicle: ").strip()
    ev = input("Is this an electric vehicle? ").strip().lower()
    msrp = float(input("Enter the MSRP: "))

    out_the_door = compute_price(msrp, make, model, ev)

    total_msrp += msrp
    total_sales_price += out_the_door

    print(f"Make: {make}")
    print(f"Model: {model}")
    print(f"MSRP: ${msrp}")
    print(f"Final Price: ${out_the_door}")

    response = input("Would you like to rerun this program?").strip().lower()

print(f"Total MSRP: ${total_msrp}")
print(f"Total Sales Price: ${total_sales_price}")