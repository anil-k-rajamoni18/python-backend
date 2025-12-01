employees = [
  {"id": 1, "name": "John", "dept_id": 10},
  {"id": 2, "name": "Sara", "dept_id": 20},
  {"id": 3, "name": "Mike", "dept_id": 10}
]

departments = [
  {"dept_id": 10, "dept_name": "Engineering"},
  {"dept_id": 20, "dept_name": "HR"}
]

innerjoinedDict={}

#Implement a manual inner join using dictionaries.
for employee in employees:
    for i, department in enumerate(departments):
        if employee["dept_id"]==department["dept_id"]
   