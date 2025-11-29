users = [
  ("john", "admin"),
  ("akash", "dev"),
  ("sara", "admin"),
  ("mike", "guest"),
]

#Convert users into dictionary
#Ensure usernames remain unique for each role
result={}
for username, role in users:
    if role not in result:
        result[role]=set()
    result[role].add(username)

for role in result:
    result[role]=list(result[role])


print(result)

#Display all admins
for key,value in result.items():
    if key=="admin":
        print(result[key])

#Add a new role "super_admin" with an empty list
result["super_admin"]=[]
print(result)


