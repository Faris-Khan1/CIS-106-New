def compute_avgs(score1, score2, score3, handicap):
    avg_score = (score1 + score2 + score3) / 3  
    average_with_handicap = avg_score + handicap  
    return avg_score, average_with_handicap  

last_name = input("Enter bowler's last name: ").strip()
score1 = float(input("Enter first game score: "))
score2 = float(input("Enter second game score: "))
score3 = float(input("Enter third game score: "))
handicap = float(input("Enter handicap: "))

avg, avg_handicap = compute_avgs(score1, score2, score3, handicap)

print(f"Bowler: {last_name}")
print(f"Average Score: {avg}")
print(f"Average Score with Handicap: {avg_handicap}")

