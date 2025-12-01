record = {"name": "John Doe", "role": "developer", "active": True}
#name=John%20Doe&role=developer&active=True
result=""
for key,value in record.items():
    value=str(value).replace(" ","%20")
    result+=f"{key}={value}&"
print(result.rstrip("&"))
