employees = ["Alice", "Amit", "Bob", "Charlie", "Catherine"]

"""
Create:

{ 
  "A": ["Alice", "Amit"], 
  "B": ["Bob"],
  "C": ["Charlie", "Catherine"]
}

"""

"""
result={}

for name in employees:
    firstletter=name[0]
    if firstletter not in result:
        result[firstletter]=[]
    result[firstletter].append(name)
print(result)

"""
result={}
for name in employees:
      result.setdefault(name[0],[]).append(name)
print(result)

#Add a new employee "Brian" dynamically
newEmployee=input("Enter the name of employee to be added: ")
"""
firstletter=newEmployee[0]
if firstletter not in result:
        result[firstletter]=[]
result[firstletter].append(newEmployee)
"""
result.setdefault(newEmployee[0],[]).add(newEmployee)
print(result)

#Sort names inside each list
for values in result.values():
    values.sort()
print(result)