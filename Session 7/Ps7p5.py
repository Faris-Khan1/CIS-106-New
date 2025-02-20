f = open("Data2.txt", "r")
total_tuition = 0
count = 0

lname = f.readline().strip()
while lname != "":
    dcode = str(f.readline().rstrip("\n"))
    credit = float(f.readline().rstrip())

    if dcode == "I":
        cost = 250
    else:
        cost = 500

    tuition = cost * credit
    count += 1
    total_tuition = total_tuition + tuition

    print(f"Student: {lname}")
    print(f"Credits taken: {credit}")
    print(f"Tuition owed: ${tuition}")
    print(f" ")

    lname = str(f.readline().rstrip("\n"))
f.close()

print(f"Number of students: {count}")
print(f"Total tuition owed: ${total_tuition}")


    


