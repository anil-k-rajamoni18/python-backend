office_employees = ["john", "sara", "mike"]
remote_employees = ["mike", "tina", "akash"]

#Find employees working both modes
employeesWorkingBothModes=[employee for employee in office_employees if employee in remote_employees]
print(f"Employees working in both the modes is {employeesWorkingBothModes}")

#Find who works only remotely
employeesWorkingOnlyRemote=[employee for employee in remote_employees if employee not in office_employees]
print(f"Employees working in remote modes is {employeesWorkingOnlyRemote}")

#Find total unique employees
uniqueEmployees=set(office_employees+remote_employees)
print(uniqueEmployees)
