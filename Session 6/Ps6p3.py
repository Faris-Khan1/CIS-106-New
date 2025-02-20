response = input("Do u want to run this program?")
count = 0

while response == "Yes":
    lname = input("Please enter last name: ")
    exam1 = float(input("Please enter score of exam 1: "))
    exam2 = float(input("Please enter score of exam 2: "))
    avg = (exam1 + exam2) / 2

    print(f"Last name: {lname}")
    print(f"average exam score: {avg}")

    count = count + 1

    response = input("Do u want to rerun the program?")

print(f"Total number of students who entered data is: {count}")
    