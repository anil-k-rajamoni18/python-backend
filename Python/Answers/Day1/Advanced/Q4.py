electricityUnitsConsumed=int(input("Enter the number of units of electricty consumed"))
if electricityUnitsConsumed<=100:
    bill=electricityUnitsConsumed*5
elif electricityUnitsConsumed>100 and electricityUnitsConsumed<=200:
    bill=100*5+(electricityUnitsConsumed-100)*7
elif electricityUnitsConsumed>200:
    bill=100*5+100*7+(electricityUnitsConsumed-200)*10    
print(bill)
    