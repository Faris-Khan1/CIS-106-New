def display_scores(lnames, scores):
    for i in range(len(lnames)):
        print(f"{lnames[i]} - {scores[i]}")

def reverse_scores(lnames, scores):
    for i in range(len(lnames) - 1, -1, -1):  
        print(f"{lnames[i]} - {scores[i]}")

lnames = ["Khan", "Philip", "Shahid", "Adam", "Hall", 
              "Paul", "Arshad", "White", "Smith", "Sharma"]

scores = [66, 49, 92, 83, 19, 69, 90, 99, 56, 81]

print("Names -- Scores")
display_scores(lnames, scores)

print("\nNames -- Scores")
reverse_scores(lnames, scores)

