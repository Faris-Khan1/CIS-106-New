class Student:
    def __init__(self, first, last, code, credits):
        self.first = first
        self.last = last
        self.code = code
        self.credits = credits

    def compute_tuition(self):
        if self.code == "I":
            tuition = self.credits * 250
        else:
            tuition = self.credits * 500
        return tuition

student_1 = Student('John', 'Doe', 'I', 15)
student_2 = Student('Jane', 'Smith', 'O', 12)

print(f"{student_1.first} {student_1.last}'s Tuition: ${student_1.compute_tuition()}")
print(f"{student_2.first} {student_2.last}'s Tuition: ${student_2.compute_tuition()}")

