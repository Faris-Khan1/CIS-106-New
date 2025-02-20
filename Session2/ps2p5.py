price = float(input("Please enter price of the item: "))
disc_perc = float(input("Please enter discount percent in decimal: "))
disc_amt = price * disc_perc
disc_price = price - disc_amt
print("The discounted amount is $ " + str(disc_amt))
print("The discounted price is $ " + str(disc_price))
