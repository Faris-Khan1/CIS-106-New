def comp_mpg(miles, gallons):
    if gallons == 0:
        return 0
    mpg = miles / gallons
    return mpg

trip = 0
response = input("Would u like to run the program?").strip().lower()

while response == "yes":
    city = input("Please enter destination: ").strip()
    miles = float(input("Please enter miles travelled: "))
    gallons = float(input("Please enter gallons used: "))

    mpg = comp_mpg(miles, gallons)

    print(f"Destination: {city}")
    print(f"Miles: {miles}")
    print(f"MPG: {mpg}")

    trip += 1
    response = input("Would u like to rerun the program?").strip().lower()

print(f"Total number of trips: {trip}")


