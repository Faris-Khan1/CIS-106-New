def compute_square_footage(length, width, height):
    floor_ceiling = 2 * length * width  
    walls_length = 2 * length * height  
    walls_width = 2 * width * height  

    total_square_footage = floor_ceiling + walls_length + walls_width
    return total_square_footage


response = input("Would you like to run this program? ").strip().lower()

while response == "yes":
    length = float(input("Enter the length of the room: "))
    width = float(input("Enter the width of the room: "))
    height = float(input("Enter the height of the room: "))

  
    square_footage = compute_square_footage(length, width, height)

    
    gallons = square_footage / 50  

   
    print(f"Total square footage: {square_footage}")
    print(f"Gallons of paint needed: {gallons}")

  
    response = input(f"Would you like to rerun the program? ").strip().lower()

print(f"End")
