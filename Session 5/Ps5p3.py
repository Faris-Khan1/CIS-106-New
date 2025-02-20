princ = float(input("Please enter principle amount: "))
years = float(input("Please enter years to maturity: "))

if princ > 100000 and years == 5:
    rate = 0.06
elif princ >= 50000 and princ <= 100000 and years == 10:
    rate = 0.05
elif princ >= 50000 and princ <= 100000 and years == 5:
    rate = 0.04
else:
    rate = 0.02
interest = princ * rate 

print(f"Principle amount: ${princ}")
print(f"interest rate: {rate * 100}%")
print(f"Interest: ${interest}")
