"""
## 1. Clean and Normalize API Response Data

You receive an API response:

```python
api_data = [
  {"id": 1, "name": "John  ", "active": "YES"},
  {"id": 2, "name": "  Priya", "active": "NO"},
  {"id": 3, "name": "Arun", "active": "YES"},
]
```

**Tasks:**
- Strip spaces in names
- Convert "YES"/"NO" to boolean values (True/False)
- Store cleaned data in a new list of dicts
- Count how many users are active
"""

api_data = [
  {"id": 1, "name": "John  ", "active": "YES"},
  {"id": 2, "name": "  Priya", "active": "NO"},
  {"id": 3, "name": "Arun", "active": "YES"},
]

user_count = 0; 
for user in api_data:
    user['name'] = user["name"].strip()
    user['active'] = True if "YES" == user['active'] else False 
    if (user['active']):
        user_count += 1

print(f" Active User Account: {user_count}")
print(api_data)
