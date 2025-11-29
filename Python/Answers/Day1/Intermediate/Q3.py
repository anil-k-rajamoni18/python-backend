number1=int(input("enter number 1: "))
number2=int(input("enter number 2: "))
number3=int(input("enter number 3: "))
if number1 > number2:
    if number1 > number3:
        print(f"{number1} is the largest")
    else:
        print(f"{number3} is the largest")
else:
    if number2> number3:
         print(f"{number2} is the largest")
    else:
         print(f"{number3} is the largest")     




