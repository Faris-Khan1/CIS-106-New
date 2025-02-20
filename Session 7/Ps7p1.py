while True:
    princ= float(input("Enter principle amount: "))
    rate = float(input("Please enter interest rate: "))

    accum_int = 0

    print(f"\n Year    Beginning Balance    Ending Balance")

    for x in range(1, 6, 1):
        ann_int = princ * rate
        end_bal = princ + ann_int
        accum_int += ann_int
         
        print(f"{x}        ${princ}             ${end_bal}")
        princ = end_bal

    print(f"\n Accumulated Interest over 5 years: ${accum_int}")