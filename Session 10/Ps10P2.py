def compute_exam(score1, score2, score3):
    total = score1 + score2 + score3
    avg = total / 3
    return total, avg

lname = input("Please enter last name: ")
score1 = float(input("Please enter exam score 1: "))
score2 = float(input("Please enter exam score 2: "))
score3 = float(input("Please enter exam score 3: "))

total, avg = compute_exam(score1, score2, score3)

print(f"Last name: {lname}")
print(f"Total exam score: {total}")
print(f"Average exam score: {avg}")
