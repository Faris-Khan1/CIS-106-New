def compute_assessed_value(county, market_value):
    if county == "Cook":
        percent = 0.90
    elif county == "Dupage":
        percent = 0.80
    elif county == "Mchenry":
        percent = 0.75
    elif county == "Kane":
        percent = 0.60
    else:
        percent = 0.70

    assessed_value = market_value * percent

    return assessed_value

response = input("Would you like to run this program? ").strip().lower()

total_market = 0
total_assessed = 0

while response == "yes":
    county = input("Enter the county: ").strip().title()  
    market_value = float(input("Enter the market value of the home: "))

    assessed_value = compute_assessed_value(county, market_value)

    print(f"County: {county}")
    print(f"Market Value: ${market_value}")
    print(f"Assessed Value: ${assessed_value}")

    total_market += market_value
    total_assessed += assessed_value

    response = input("Would you like to rerun the program? ").strip().lower()

print(f"Total Market Value: ${total_market}")
print(f"Total Assessed Value: ${total_assessed}")

