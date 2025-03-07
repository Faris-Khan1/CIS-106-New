line = input("Enter a line of comma separated values: ")

values = line.split(",")

for value in values:
    print(f"{value.strip()}")
