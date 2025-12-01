amount=float(input("Enter the amount: "))
taxrate=float(input("Enter the taxrate: "))
finalbill=amount+(taxrate/100)*amount
print(f"final bill is {finalbill}")