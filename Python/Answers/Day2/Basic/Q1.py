userNameStored="Navya"
passwordStored="Navya123"

noofChances=1
while(noofChances<=3):
    userName=input("Enter username: ")
    password=input("Enter Password: ")
    if userName==userNameStored and password==passwordStored:
            print("Attempt Succesful")
            break
    
     
    else:
          print("Incorrect credentials, try again")
          noofChances+=1
if noofChances>3:
      print("Account locked")
