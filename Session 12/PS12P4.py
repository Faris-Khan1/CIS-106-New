def display_players(names, averages):
    for i in range(len(names)):
        print(f"{names[i]} -- {averages[i]}")

def search_player(names, averages, lastname):
    if lastname in names:
        index = names.index(lastname)
        print(f"{lastname} -- {averages[index]}")

f = open("players.txt", "r")

names = []
averages = []

for line in f:
    parts = line.strip().split(",")
    names.append(parts[0].strip())
    averages.append(float(parts[1].strip()))

f.close()

while True:
    lastname = input("Enter a player's last name: ").strip()
    search_player(names, averages, lastname)


