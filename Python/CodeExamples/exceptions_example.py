from datetime import date
import requests

print("Welcome to Exception Handling")

try:
    num1 = int(input("Enter Num1:"))
    num2 = int(input("Enter Num2:"))
    print(f"Division Of {num1}/{num2} = {num1/num2}")
except (ValueError, ZeroDivisionError) as e:
    print("Exception Handled..", e)

print(f"Today: ", date.today())
print("Division Operation Completed")


api_endpoint = "https://open-weather13.r.rapidapi.com/CITY"
headers = {"x-rapidapi-host" : "open-weather13.p.rapidapi.com" ,
"x-rapidapi-key" : "bfa73a12a8msh0fd2368b057d757p19201ajsnd017d538d45b"
}

payload = {"city" : "gwalior",
"lang" : "EN"
}
try:
    response = requests.get(url=api_endpoint, headers=headers, params=payload)
    print(f"status code: {response.status_code}")
    print(f"weather data: {response.json()}")
except Exception as e:
    print({"error": "API failed"})
    print(f"Exception: {e}")

print("End")


class InvalidAgeError(Exception):
    pass

def register(age):
    if age < 18:
        raise InvalidAgeError("Age must be 18+")
    print("registered")

register(18)
try:
    register(11)
except InvalidAgeError as e:
    print(e, "Please pass valid age")