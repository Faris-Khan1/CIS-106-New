class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = float(pay)
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return f"{self.first} {self.last}"

    def bonus(self, rate):
        return self.pay * rate


class Manager(Employee):
    def long_term_bonus(self):
        return self.pay * 0.50  


class Executive(Employee):
    def long_term_bonus(self):
        return self.pay * 0.50 

    def executive_bonus(self):
        return self.pay * 2.00  


mgr = Manager("Nathan", "Smith", 80000)
exec = Executive("Faris", "Khan", 120000)

print(f"{mgr.fullname()}")
print(f"Manager Long-term Bonus: ${mgr.long_term_bonus()}")

print(f"\n{exec.fullname()}")
print(f"Executive Long-term Bonus: ${exec.long_term_bonus()}")
print(f"Executive Bonus: ${exec.executive_bonus()}")


