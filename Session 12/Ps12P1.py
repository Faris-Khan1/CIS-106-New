def display_names(lnames):
    for name in lnames:
        print(name)

def reverse(lnames):
    for i in range(len(lnames) - 1, -1, -1):  
        print(lnames[i])

lnames = ["Khan", "Philip", "Shahid", "Adam", "Hall", 
              "Paul", "Arshad", "White", "Smith", "Sharma"]

print("Names in original order:")
display_names(lnames)

print("\nNames in reverse order:")
reverse(lnames)

