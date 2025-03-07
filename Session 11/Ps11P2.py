line = input("Enter a line of text: ")

newtext = " ".join(line.split())

print(f"{newtext[::-1]}")
