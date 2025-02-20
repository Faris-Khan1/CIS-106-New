def compute_tuition(credit_hours, district_code):
    if district_code == "I":  
        rate = 250
    else:  
        rate = 550

    tuition = credit_hours * rate  
    return tuition  

total_tuition = 0

response = input("Would you like to run this program? ").strip().lower()

while response == "yes":  
    lname = input("Please enter student's last name: ").strip()
    credit_hours = float(input("Please enter credit hours: "))
    district_code = input("Enter district code: ").strip()

    tuition = compute_tuition(credit_hours, district_code)  

    print(f"Student: {lname}")
    print(f"Tuition Owed: ${tuition}")

    total_tuition += tuition  

    response = input("Would you like to rerun this program? ").strip().lower()

print(f"Total tuition owed by all students: ${total_tuition}")
