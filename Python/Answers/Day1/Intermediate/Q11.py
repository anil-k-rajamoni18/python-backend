emailAddress=input("enter the email: ")
"""
result=emailAddress.split("@")
print(f"domain is {result[1]}")
 """
""" domain=emailAddress.split("@")[1]
print(domain)
"""

print(emailAddress[emailAddress.find("@")+1:])
