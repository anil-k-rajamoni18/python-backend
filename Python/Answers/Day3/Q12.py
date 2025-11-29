permissions = {
  "admin": {"read", "write", "delete"},
  "dev": {"read", "write"},
  "guest": {"read"}
}

#Check if dev is allowed to delete
isDevAllowedtoDelete= "delete" in permissions["dev"] 
print(isDevAllowedtoDelete)

#List permissions missing in guest compared to admin
permissionMissinginGuest=[permission for permission in permissions["admin"] if permission not in permissions["guest"]]
print(permissionMissinginGuest)

#Create a set of all unique permissions used in system
"""

uniquePermissions=set()

for permission in permissions.values():
    for value in permission:
     uniquePermissions.add(value)
print(uniquePermissions)

"""
uniquePermissions=set().union(*permissions.values())
print(uniquePermissions)