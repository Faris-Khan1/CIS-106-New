def display_names_and_scores(lnames, scores):
    for i in range(len(lnames)):
        print(f"{lnames[i]} -- {scores[i]}")

def find_highest_lowest(lnames, scores):
    high_var = 0  
    low_var = 999  
    
    high_index = 0
    low_index = 0   

    for i in range(len(scores)):
        if scores[i] > high_var:
            high_var = scores[i]
            high_index = i
        
        if scores[i] < low_var:
            low_var = scores[i]
            low_index = i

    print(f"Highest Score: {lnames[high_index]} -- {high_var}")
    print(f"Lowest Score: {lnames[low_index]} -- {low_var}")

def main():
    f = open("Data3.txt", "r")

    lname = []
    scores = []

    lastname = f.readline().strip()
    
    while lastname != "": 
        score = f.readline().strip() 
        
        lname.append(lastname)
        scores.append(int(score)) 
        
        lastname = f.readline().strip() 

    f.close()  

    print("Results:")
    find_highest_lowest(lname, scores)

main()


