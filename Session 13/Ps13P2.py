class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last 
        self.pay = float(pay)
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def bonus(self, rate):
        bonus_amount = self.pay * rate
        return bonus_amount

emp_1 = Employee('Faris', 'Khan', '60000')
emp_2 = Employee('Test', 'User', '50000')

bonus_rate = float(input("Enter the bonus rate: "))

print(f"Bonus for {emp_1.fullname()}: ")
print(f"Bonus for {emp_2.fullname()}: ")

