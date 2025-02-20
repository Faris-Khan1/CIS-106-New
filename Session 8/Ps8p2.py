def comp_bat_avg(hits, atbats):
    if atbats == 0:
        return 0

    batting_avg = hits / atbats
    return batting_avg

count = 0
response = input("Would u like to run the program?")

while response == "Yes":
    lname = input("Please enter last name: ").strip()
    hits = int(input("Please enter number of hits: "))
    atbats = int(input("Please enter number of at-bats: "))

    avg = comp_bat_avg(hits, atbats)

    print(f"Player: {lname}")
    print(f"Batting average: {avg}")
    count += 1

    response = input("Would u like to rerun the program?")

print(f"Total number of players: {count}")

