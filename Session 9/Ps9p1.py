def compute_forecast(month, sales):
    forecast = 0  

    if month == "jan" or month == "feb" or month == "mar":
        forecast = 0.10
    elif month == "apr" or month == "may" or month == "jun":
        forecast = 0.15
    elif month == "jul" or month == "aug" or month == "sep":
        forecast = 0.20
    elif month == "oct" or month == "nov" or month == "dec":
        forecast = 0.25

    next_month = sales * (1 + forecast)  

    return next_month

response = input("Would you like to run this program? ").strip().lower()

while response == "yes":
    lname = input("Please enter last name: ").strip()
    month = input("Please enter the month: ").strip().lower()
    sales = float(input("Please enter total sales: "))

    sales_forecast = compute_forecast(month, sales)

    print(f"Employee: {lname}")
    print(f"Month: {month}")
    print(f"Sales: ${sales}")
    print(f"Next month forecast: ${sales_forecast}")

    response = input("Would you like to rerun this program? ").strip().lower()

print(f"End")
