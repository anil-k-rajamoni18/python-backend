emailAddress=input("Enter the email address: ")
if "@" in emailAddress and "." in emailAddress:
    if emailAddress.index("@")<emailAddress.index("."):
        print("Valid Email")
    else:
        print("Invalid Email")
else:
    print("Invalid Email")