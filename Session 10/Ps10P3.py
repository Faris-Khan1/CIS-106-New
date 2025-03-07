def compute_commission(sales):
    if sales > 100000:
        commission = sales * 0.10
    else:
        commission = sales * 0.05 
    
    next_year_target = sales * 1.05  
    return commission, next_year_target  

last_name = input("Enter last name: ").strip()
sales = float(input("Enter total sales amount: "))

commission, next_year_target = compute_commission(sales)

print(f"Last name: {last_name}")
print(f"Commission Earned: ${commission}")
print(f"Next Year's Target: ${next_year_target}")


