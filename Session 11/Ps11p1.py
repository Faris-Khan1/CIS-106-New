name = input("Please enter full name: ").strip()

cut = name.split()

if len(cut) != 2:
    print(f"Invalid! Please enter first and last name only")
else:
    first_name = cut[0]
    last_name = cut[1]

    first_init = first_name[0].upper()
    last_name = last_name.capitalize()
    print(f"{last_name}, {first_init}")
