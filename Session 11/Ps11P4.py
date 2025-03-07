text = input("Please enter a line of text: ")
char = int(input("Enter number of characters per line: "))
lines = int(input("Enter number of lines: "))
scroll = input("Enter scroll direction: ").strip().lower()

repeat = (text * (char // len(text) + 1))[:char]

for i in range(lines):
    if scroll == "left":
        shift = repeat[i:] + repeat[:i]
    elif scroll == "right":
        shift = repeat[-i:] + repeat[:-i]
    else:
        print("Invalid direction")

    print(shift)

