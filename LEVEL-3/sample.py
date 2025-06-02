import requests 

endpoint = "https://reqres.in/api/users?page=2"

api_response = requests.get(endpoint)
print(api_response.status_code)
print(api_response.json())

# extract last_name and first_name and combine to full_name and also extract email
# create users.csv and write full_name, email 
